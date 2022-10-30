from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(max_length=255, label="Username")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username has been taken.")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used.")

    class Meta:
        model = User
        fields = ("username", "email", )
