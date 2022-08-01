
from email.message import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from buyer.forms import RegisterForm

from order.forms import OrderVarifyForm

# from luckydraw.models import LuckyDraws, Drawables
from .models import Buyer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.contrib.auth import login
from interiorshop import settings


# Create your views here.
from order.models import OrderItem, Order, OrderStatusEnum


def become_buyer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            buyer = Buyer.objects.create(name=user.username, created_by=user)
            login(request, user)

            send(request)
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'buyer/become_buyer.html', {'form': form})


def get_paid_amount(b):
    sum = 0
    orderItem = OrderItem.objects.all()
    for order in orderItem:
        if order.buyer == b.name:
            sum += (order.price*order.quantity)
    return sum


@login_required
def profile(request):
    buyer = request.user.buyer
    ## Editing Profile

    if request.method == 'POST':
        complete_name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')

        buyer.created_by.email = email
        buyer.created_by.save()

        buyer.complete_name = complete_name
        buyer.phone = phone
        buyer.address = address
        buyer.city = city
        buyer.save()

        return redirect('profile')
    return render(request, 'buyer/buyer_profile.html', {'buyer': buyer})
def viewOrders(request):
    buyer = request.user.buyer
    order = OrderItem.objects.filter(buyer=buyer)
    value = get_paid_amount(buyer)
    return render(request, 'buyer/total-orders.html', {'order': order,'value':value})

def viewOrdersVarified(request):
    buyer = request.user.buyer
    order = OrderItem.objects.filter(buyer=buyer)
    value = get_paid_amount(buyer)
    return render(request, 'buyer/varified-order.html', {'order': order,'value':value})

def viewOrdersNotVarified(request):
    buyer = request.user.buyer
    order = OrderItem.objects.filter(buyer=buyer)
    value = get_paid_amount(buyer)
    return render(request, 'buyer/notvarified-order.html', {'order': order,'value':value})

def viewOrdersDelivered(request):
    buyer = request.user.buyer
    order = OrderItem.objects.filter(buyer=buyer)
    value = get_paid_amount(buyer)
    return render(request, 'buyer/delivered-order.html', {'order': order,'value':value})

def viewOrderVarify(request):
    buyer = request.user.buyer
    order = OrderItem.objects.filter(buyer=buyer)
    value = get_paid_amount(buyer)
    return render(request, 'buyer/varify-orders.html', {'order': order,'value':value})

def varifyOrder(request,pk):
    # print(pk)
    order=get_object_or_404(Order,pk=pk)
    form = OrderVarifyForm(instance=order)
    if request.method=='POST':
        slip = request.POST.get('paid_slip', '')
        order.paid_slip=slip
        order.save()
        # return redirect('varify-order')
    else:
        form = OrderVarifyForm(instance=order)
    return render(request, 'buyer/varify.html',{'form':form,'order':order})

def send(request):
    from_email = settings.EMAIL_HOST_USER

    to_email = request.user.email
    subject = 'Signup Successful'
    text_content = 'Thank you for the order!'
    html_content = render_to_string(
        'buyer/email_notify_signup.html')

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()



