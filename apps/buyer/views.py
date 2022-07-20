
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# from apps.luckydraw.models import LuckyDraws, Drawables
from .models import Buyer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.conf import settings


# Create your views here.
from ..order.models import OrderItem, Order


def become_buyer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            buyer = Buyer.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

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
    subject = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anmirza68@gmail.com']
    #send=send_mail( subject, message, email_from, recipient_list )
    html_temp = "buyer/msg.html"
    html_msg = render_to_string(html_temp)
    msgs = EmailMultiAlternatives(
        subject, html_msg, email_from, recipient_list)
    msgs.attach_alternative(html_msg, "text/html")
    order = OrderItem.objects.all()
    value = get_paid_amount(buyer)
    return render(request, 'buyer/buyer_profile.html', {'buyer': buyer, 'order': order, 'value': get_paid_amount(buyer)})


def send(link, email):
    subject = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anmirza68@gmail.com']
    #send=send_mail( subject, message, email_from, recipient_list )
    html_temp = '<a href="{% url home %}">hh</a>'
    html_msg = render_to_string(html_temp, {'link': link})
    msg = EmailMultiAlternatives(subject, html_msg, email_from, recipient_list)
    msg.content_subtype = 'html'
    msg.send()
    return HttpResponse('redirect to a new page')


@login_required
def edit_profile(request):
    buyer = request.user.buyer

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            buyer.created_by.email = email
            buyer.created_by.save()

            buyer.name = name
            buyer.save()

            return redirect('buyer_profile')

    return render(request, 'buyer/edit_profile.html', {'buyer': buyer})
