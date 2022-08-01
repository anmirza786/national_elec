from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from product.models import Product, ProductImage


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'accept': '.png'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the Complete '
                                                                                         'Description of the '
                                                                                         'Product'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Price'}),
        }


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'UserName'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'Email'}),
        }
