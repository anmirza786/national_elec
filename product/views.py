import random
from cart.cart import Cart
from django.db.models import Q
from .forms import AddToCartForm
from django.contrib import messages
from .models import Category, Product
from .models import ProductStatusEnum
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect


def search(request):
    query = request.GET.get('search', '')
    products = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query))
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    categories = Category.objects.all()
    return render(request, 'product/search.html', {'query': query, 'page_obj': page_obj, 'product': paginator, 'pages': pages, 'categories': categories})


def product(request, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug)

    imagesstring = '{"thumbnail": "%s", "image": "%s", "id": "mainimage"},' % (
        product.get_thumbnail(), product.image.url)

    for image in product.images.all():
        imagesstring += ('{"thumbnail": "%s", "image": "%s", "id": "%s"},' %
                         (image.get_thumbnail(), image.image.url, image.id))

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            varient = form.cleaned_data['varient']
            if request.user.is_authenticated:
                cart.add(product_id=product.id,
                         quantity=quantity, product_varient=varient, update_quantity=False)

                messages.success(request, 'The product was added to the cart')

                return redirect('product', category_slug=category_slug, product_slug=product_slug)
            else:
                return redirect('login')
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    categories = Category.objects.all()
    context = {
        'form': form,
        'product': product,
        'similar_products': similar_products,
        'imagesstring': "[" + imagesstring.rstrip(',') + "]",
        'categories': categories
    }
    return render(request, 'product/product.html', context)


def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    values = Category.objects.all().values()
    subcat = []
    product = []
    if category.catlevel == 1:
        for values in values:
            if values['catlevel'] == 2:

                if values['parent_id'] == category.id:
                    id = values['id']
                    subcat = Category.objects.filter(parent_id=category.id)
                    print(subcat)
                    c = Category.objects.get(id=id)
                    p = Product.objects.filter(category=c)
                    for p in p:
                        product.append(p)
    else:
        product = Product.objects.filter(category=category)

    if product:
        paginator = Paginator(product, 9)
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
            pages = paginator.page(page_number)
        except:
            page_obj = paginator.get_page(1)
            pages = paginator.page(1)
    categories = Category.objects.all()
    return render(request, 'product/category.html', {'category': category, 'page_obj': page_obj, 'product': paginator, 'pages': pages, 'subcat': subcat, 'categories': categories})


def veiwProducts(request):
    product = Product.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/view_products.html', {'page_obj': page_obj, 'product': paginator, 'pages': pages, 'categories': categories})


def veiwProductsSoon(request):
    product = Product.objects.filter(product_status=ProductStatusEnum.SOON)
    categories = Category.objects.all()

    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/view_products_soon.html', {'page_obj': page_obj, 'product': paginator, 'pages': pages, 'categories': categories})


def veiwProductsAvailable(request):
    product = Product.objects.filter(
        product_status=ProductStatusEnum.AVAILABLE)
    categories = Category.objects.all()

    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/view_products_available.html', {'page_obj': page_obj, 'product': paginator, 'pages': pages, 'categories': categories})


def veiwProductsStock(request):
    product = Product.objects.filter(
        product_status=ProductStatusEnum.OUTOFSTOCK)
    categories = Category.objects.all()

    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request, 'product/view_products_stock.html', {'page_obj': page_obj, 'product': paginator, 'pages': pages, 'categories': categories})
