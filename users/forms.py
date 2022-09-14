from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# rewrite UserCreationForm with adding email field
class UsersForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']
