import random

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductStatusEnum
from .forms import AddToCartForm
from .models import Category, Product

from apps.cart.cart import Cart

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    paginator = Paginator(products,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/search.html', {'query': query,'page_obj':page_obj,'product':paginator,'pages':pages})

def product(request, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    imagesstring = '{"thumbnail": "%s", "image": "%s", "id": "mainimage"},' % (product.get_thumbnail(), product.image.url)

    for image in product.images.all():
        imagesstring += ('{"thumbnail": "%s", "image": "%s", "id": "%s"},' % (image.get_thumbnail(), image.image.url, image.id))
    
    # print(imagesstring)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            print(quantity)
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        'form': form,
        'product': product,
        'similar_products': similar_products,
        'imagesstring': "[" + imagesstring.rstrip(',') + "]"
    }

    return render(request, 'product/product.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    # print(product)
    paginator = Paginator(product,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/category.html', {'category': category,'page_obj':page_obj,'product':paginator,'pages':pages})

def veiwProducts(request):
    product = Product.objects.all()
    # print(product)
    paginator = Paginator(product,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsSoon(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.SOON)
    # print(product)
    paginator = Paginator(product,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_soon.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsAvailable(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.AVAILABLE)
    # print(product)
    paginator = Paginator(product,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_available.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsStock(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.OUTOFSTOCK)
    # print(product)
    paginator = Paginator(product,9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_stock.html',{'page_obj':page_obj,'product':paginator,'pages':pages})
