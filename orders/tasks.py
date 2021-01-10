''' Asynchronous task to send order email notification '''
from celery import shared_task
from django.core.mail import send_mail
from account.models import User
from .models import Order

@shared_task
def order_created(order_id):
    ''' Task to send an e-mail notification to customer when an order is successfully created. '''
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
               Your order id is {}.'.format(order.user.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@nowwegrow.com',
                          [order.user.email])
    return mail_sent

@shared_task
def merchant_notify(order_id, user_id, emails):
    ''' Task to send an e-mail notification to merchants when an order is successfully created. '''
    user = User.objects.get(id=user_id)
    subject = 'Order # {}'.format(order_id)
    message = 'Hello,\n\nYou have sold a product to {}.\
               Please check your dashboard for further details regarding order number {}.'.format(user.get_full_name(), order_id)
    
    mail_sent = send_mail(subject, message, 'admin@nowwegrow.com', emails)

    return mail_sent