from site import getuserbase
from interiorshop import settings
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


def notify_customer(order):
    from_email = settings.EMAIL_HOST_USER

    to_email = order.buyer.created_by.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string(
        'order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
