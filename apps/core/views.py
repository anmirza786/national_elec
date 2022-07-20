from email import message
from django.shortcuts import redirect, render
from apps.cart.cart import Cart
from apps.core.forms import ContactForm, FeedbackForm
from apps.core.models import Contact, Feedback

from apps.product.models import Product,Category
import random

def frontpage(request):
    newest_products = Product.objects.all()[0:4]
    # cart = Cart(request)
    random_products = list(Product.objects.all())
    # print(random_products.__len__())
    if random_products.__len__()>=10:
        random_products = random.sample(random_products,10)
    else:
        random_products = random.sample(random_products,random_products.__len__())
    categories = Category.objects.all()
    return render(request, 'core/frontpage.html', {'newest_products': newest_products,'random_products':random_products,'categories':categories})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            vendor = Contact.objects.create(
                name=contact.name, email=contact.email, message=contact.message)

            return redirect('frontpage')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save()

            vendor = Feedback.objects.create(
                name=feedback.name, feedback=feedback.feedback)

            return redirect('frontpage')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback.html',{'form':form})
