from django.urls import path

from . import views

urlpatterns = [
    path('', views.veiwProducts, name='products'),
    path('available/', views.veiwProductsAvailable, name='available'),
    path('soon/', views.veiwProductsSoon, name='soon'),
    path('out_of_stock/', views.veiwProductsStock, name='stock'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]
