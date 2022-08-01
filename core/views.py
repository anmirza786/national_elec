from email import message
from django.shortcuts import redirect, render
from cart.cart import Cart

from core.models import Contact,PopularClients

from product.models import Product,Category
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
    g=Product.objects.all()
    for g in g:
        print(g.title,'\t',g.image)
    clients = PopularClients.objects.all()
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)

    return render(request, 'core/frontpage.html', {'newest_products': newest_products,'random_products':random_products,'categories':categories,'clients':clients})

