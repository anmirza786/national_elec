"""esmartapp_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.become_buyer, name='signup'),
    path('total-orders/', views.viewOrders, name='total-orders'),
    path('varified-orders/', views.viewOrdersVarified, name='varified-orders'),
    path('varify-order/', views.viewOrderVarify, name='varify-order'),
    path('varify-order/varify/<int:pk>', views.varifyOrder, name='varify'),
    path('notvarified-orders/', views.viewOrdersNotVarified, name='notvarified-orders'),
    path('delivered-orders/', views.viewOrdersDelivered, name='delivered-orders'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='buyer/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="buyer/reset-password.html"), name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="buyer/reset-password-sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="buyer/reset-password-form.html"), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="buyer/reset-password-done.html"), name="password_reset_complete"),
]
