from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from .models import CustomUser


class SignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    conf_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'phone_number',
            'password'
        ]

    def clean(self):
        username = self.cleaned_data.get('username')

        if username and username[0].isdigit():
            raise ValidationError('Username raqam bilan boshlanmasin')

        if len(username) < 5:
            raise ValidationError('Username kamida 5 ta belgidan iborat bolishi kerak')

        return username

    