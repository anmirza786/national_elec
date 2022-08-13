from urllib import request
import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from product.models import Category

from .cart import Cart
from .forms import CheckoutForm

from order.utilities import checkout, notify_customer


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        current_user = request.user.buyer
        categories = Category.objects.all()
        print(current_user)

        if request.method == 'POST':
            complete_name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '')

            current_user.created_by.email = email
            current_user.created_by.save()

            current_user.complete_name = complete_name
            current_user.phone = phone
            current_user.address = address
            current_user.city = city
            current_user.save()
            order = checkout(request, cart.get_total_cost(), current_user)

            cart.clear()
            # notify_customer(order)

            return redirect('success')
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

    return render(request, 'cart/cart.html', {'categories':categories})


def success(request):
    categories = Category.objects.all()
    
    return render(request, 'cart/success.html',{'categories':categories})
