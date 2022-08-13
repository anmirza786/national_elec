from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('buyer_name', 'buyer_phone', 'buyer_address',
                    'buyer_city', 'order_status', 'created_at', 'paid_amount')
    list_filter = ('order_status', )

    @admin.display(description='Buyer Name', ordering='buyer__name')
    def buyer_name(self, obj):
        return obj.buyer.complete_name

    @admin.display(description='Buyer phone', ordering='buyer__phone')
    def buyer_phone(self, obj):
        return obj.buyer.phone

    @admin.display(description='Buyer city', ordering='buyer__city')
    def buyer_city(self, obj):
        return obj.buyer.phone

    @admin.display(description='Buyer address', ordering='buyer__address')
    def buyer_address(self, obj):
        return obj.buyer.address


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'buyer', 'quantity', 'price')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
