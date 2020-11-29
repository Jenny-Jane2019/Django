from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User



# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm
from .decorators import allowed_users
import os


def home(request): #添加对应的处理方法
    return render(request, 'APP/index.html')


def recognition(request): #添加对应的处理方法
    return render(request, 'APP/recognition.html')


def upload(request): #添加对应的处理方法
    if request.user.is_authenticated:
        username = request.user.username
    user = User.objects.get(username=username)
    customer = Customer(user=user)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        count = Customer.objects.filter(user=request.user).count()
        if count > 10:
            messages.add_message(request, messages.INFO, "You have already uploaded too many files！")
        else:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, "successfully!")
                return redirect("file_list")
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request, 'APP/upload.html', context)


def file_list(request):
    files = Customer.objects.filter(user=request.user)
    count = Customer.objects.filter(user=request.user).count()
    if count == 0:
        messages.info(request, "No files uploaded yet!")
    return render(request, 'APP/file_list.html', {'files': files})


def loginPage(request):#添加对应的处理方法
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'APP/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group =Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form': form}
        return render(request, 'APP/register.html', context)