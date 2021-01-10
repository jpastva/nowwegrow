''' Views for payment app '''
import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from orders.models import Order, OrderItem
from orders.tasks import order_created, merchant_notify
from account.models import Membership, MerchantProfile

def payment_process(request):
    ''' View to process payment via Braintree after order creation '''
    order_id = request.session.get('order_id')
    member_id = request.session.get('member_id')
    order = get_object_or_404(Order, id=order_id)
    # For sending order notice to merchants
    emails_dict = list(OrderItem.objects.filter(order=order).values('product__merchant__email'))
    # Extract email addresses from dicts
    emails = [li['product__merchant__email'] for li in emails_dict]

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid and active
            order.paid = True
            order.active = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            # launch asynchronous tasks to notify customer and merchants
            order_created.delay(order.id)
            merchant_notify.delay(order.id, request.user.id, emails)
            
            # check for membership payment
            if member_id is not None:
                member = Membership.objects.get(id=member_id)
                merchant = MerchantProfile.objects.get(user = request.user)
                member.active = True
                member.save()
                merchant.is_active = True
                merchant.save()

            return redirect('payment:done')
        else:
            # Bad payment
            order.active = False
            order.save()
            # Send order info for payment retry
            request.session['order_id'] = order.id
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(request, 
                      'payment/process.html', 
                      {'order': order,
                       'client_token': client_token})

def payment_done(request):
    ''' View to render payment complete page '''
    return render(request, 'payment/done.html')

def payment_canceled(request):
    ''' View to render payment problem page '''
    if request.method == 'POST':
        order = Order.objects.get(id=request.POST.get('order_id'))
        request.session['order_id'] = order.id
        # redirect for payment
        return redirect(reverse('payment:process'))
    else:
        order_id = request.session.get('order_id')
        return render(request, 'payment/canceled.html', {'order_id': order_id})
