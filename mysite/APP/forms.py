from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['speaker_name', 'speaker_sex', 'speaker_age', 'phone_type', 'geography', 'environment', 'file']


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['overlap']

