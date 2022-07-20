from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer','order_status', 'created_at', 'paid_amount')
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'buyer','quantity','price')

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
