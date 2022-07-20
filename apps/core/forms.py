from django import forms
from .models import Contact, Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the Complete '
                                             'Message '
                                             }),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the Complete '
                                              'Feedback '
                                              }),
        }
