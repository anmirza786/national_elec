from urllib import request
import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .cart import Cart
from .forms import CheckoutForm

from apps.order.utilities import checkout, notify_customer, notify_vendor


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        current_user = request.user.buyer
        print(current_user)

        if request.method == 'POST':
                stripe.api_key = settings.STRIPE_SECRET_KEY

                try:

                    order = checkout(request, cart.get_total_cost(), current_user)

                    cart.clear()

                    notify_customer(order)
                    notify_vendor(order)

                    return redirect('success')
                except Exception:
                    messages.error(
                        request, 'There was something wrong with the payment')
        else:
            form = CheckoutForm()
    else:
        return redirect('login')
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html', {'stripe_pub_key': settings.STRIPE_PUB_KEY})


def success(request):
    return render(request, 'cart/success.html')
