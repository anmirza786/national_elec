from django.db import models
from apps.buyer.models import Buyer

from apps.product.models import Product
# from apps.vendor.models import Vendor
from django.contrib.auth import get_user_model
User = get_user_model()

class OrderStatusEnum(models.IntegerChoices):
    VARIFICATIONPENDING = 1, 'Varification Pending'
    VARIFIED = 2, 'Varified'
    DELIVERED = 3, 'Delivered'


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='orders')
    total = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=True,
                                blank=True)
    status = models.SmallIntegerField(max_length=30,
                                      choices=OrderStatusEnum.choices,
                                      default=OrderStatusEnum.VARIFICATIONPENDING)
    order_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=21, default='')
    address = models.CharField(max_length=256, default='')
    town = models.CharField(max_length=56, default='')
    postalcode = models.CharField(max_length=11, default='')

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    def get_total_price(self):
        return self.price * self.quantity
