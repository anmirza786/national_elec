from dataclasses import field
from pyexpat import model
from django import forms
from .models import Order

class OrderVarifyForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['paid_slip']
        widgets = {
            'paid_s;ip': forms.FileInput(),
        }