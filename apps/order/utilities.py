from site import getuserbase
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.cart.cart import Cart

from .models import Order, OrderItem


def checkout(request, amount,user):
    order = Order.objects.create(buyer=user, paid_amount=amount)

    for item in Cart(request):
        OrderItem.objects.create(
            order=order, product=item['product'],buyer=user, price=item['product'].price, quantity=item['quantity'])

    return order


def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for vendor in order.vendors.all():
        to_email = vendor.created_by.email
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string(
            'order/email_notify_vendor.html', {'order': order, 'vendor': vendor})

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string(
        'order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
