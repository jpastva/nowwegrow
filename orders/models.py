''' Models for orders app, including Order, OrderItem '''
from django.db import models
from shop.models import Product
from register.models import User

class Order(models.Model):
    ''' Model to store order data '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    address = models.ForeignKey('account.Address', blank=False, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    ''' Model to store items for orders '''
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity