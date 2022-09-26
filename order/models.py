from django.db import models
from buyer.models import Buyer

from product.models import Product
# from vendor.models import Vendor
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderStatusEnum(models.IntegerChoices):
    VARIFIED = 1, 'Varified'
    NOTVARIFIED = 2, 'Not Varified'
    DELIVERED = 3, 'Delivered'


class Order(models.Model):
    buyer = models.ForeignKey(
        Buyer, related_name='order_buyer', on_delete=models.SET_NULL, null=True)
    order_status = models.SmallIntegerField(
        choices=OrderStatusEnum.choices, default=OrderStatusEnum.NOTVARIFIED)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_slip = models.FileField(blank=True, upload_to='slips/')
    # vendors = models.ManyToManyField(Vendor, related_name='orders')

    class Meta:
        ordering = ['-created_at']
    # def save(self):
    #     # item=OrderItem.objects.filter(order_id=self.id)
    #     # if self.order_status == OrderStatusEnum.DELIVERED:

    #     return super().save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='productitems', on_delete=models.CASCADE)
    product_varient = models.CharField(null=True, blank=True, max_length=255)
    buyer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    def get_total_price(self):
        return self.price * self.quantity
