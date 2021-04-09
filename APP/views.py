from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
import librosa.display
import numpy as np
import base64
from io import BytesIO
import matplotlib.pyplot as plt



# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm, MapForm
from .decorators import allowed_users
import os


def home(request): #添加对应的处理方法
    return render(request, 'APP/index.html')


def library(request): #添加对应的处理方法
    return render(request, 'APP/library.html')


def geography(request): #添加对应的处理方法
    customer = Customer.objects.all()
    total = customer.count()
    female = customer.filter(speaker_sex="female")
    num_f = female.count()
    male = customer.filter(speaker_sex="male")
    num_m = male.count()
    list1 = []
    list2 = []
    p = female.filter(geography="Beijing").count()
    list1.append(p)
    p = female.filter(geography="Tianjin").count()
    list1.append(p)
    p = female.filter(geography="Shanghai").count()
    list1.append(p)
    p = female.filter(geography="Chongqing").count()
    list1.append(p)
    p = female.filter(geography="Hebei").count()
    list1.append(p)
    p = female.filter(geography="Henan").count()
    list1.append(p)
    p = female.filter(geography="Yunnan").count()
    list1.append(p)
    p = female.filter(geography="Liaoning").count()
    list1.append(p)
    p = female.filter(geography="Heilongjiang").count()
    list1.append(p)
    p = female.filter(geography="Hunan").count()
    list1.append(p)
    p = female.filter(geography="Anhui").count()
    list1.append(p)
    p = female.filter(geography="Shandong").count()
    list1.append(p)
    p = female.filter(geography="Xinjiang").count()
    list1.append(p)
    p = female.filter(geography="Jiangsu").count()
    list1.append(p)
    p = female.filter(geography="Zhejiang").count()
    list1.append(p)
    p = female.filter(geography="Jiangxi").count()
    list1.append(p)
    p = female.filter(geography="Hubei").count()
    list1.append(p)
    p = female.filter(geography="Guangxi").count()
    list1.append(p)
    p = female.filter(geography="Gansu").count()
    list1.append(p)
    p = female.filter(geography="Shanxi").count()
    list1.append(p)
    p = female.filter(geography="Inner Mongolia").count()
    list1.append(p)
    p = female.filter(geography="Shaanxi").count()
    list1.append(p)
    p = female.filter(geography="Jilin").count()
    list1.append(p)
    p = female.filter(geography="Fujian").count()
    list1.append(p)
    p = female.filter(geography="Guizhou").count()
    list1.append(p)
    p = female.filter(geography="Guangdong").count()
    list1.append(p)
    p = female.filter(geography="Qinghai").count()
    list1.append(p)
    p = female.filter(geography="Tibet").count()
    list1.append(p)
    p = female.filter(geography="Sichuan").count()
    list1.append(p)
    p = female.filter(geography="Ningxia").count()
    list1.append(p)
    p = female.filter(geography="Hainan").count()
    list1.append(p)
    p = female.filter(geography="Taiwan").count()
    list1.append(p)
    p = female.filter(geography="Hong Kong").count()
    list1.append(p)
    p = female.filter(geography="Macao").count()
    list1.append(p)

    p = male.filter(geography="Beijing").count()
    list2.append(p)
    p = male.filter(geography="Tianjin").count()
    list2.append(p)
    p = male.filter(geography="Shanghai").count()
    list2.append(p)
    p = male.filter(geography="Chongqing").count()
    list2.append(p)
    p = male.filter(geography="Hebei").count()
    list2.append(p)
    p = male.filter(geography="Henan").count()
    list2.append(p)
    p = male.filter(geography="Yunnan").count()
    list2.append(p)
    p = male.filter(geography="Liaoning").count()
    list2.append(p)
    p = male.filter(geography="Heilongjiang").count()
    list2.append(p)
    p = male.filter(geography="Hunan").count()
    list2.append(p)
    p = male.filter(geography="Anhui").count()
    list2.append(p)
    p = male.filter(geography="Shandong").count()
    list2.append(p)
    p = male.filter(geography="Xinjiang").count()
    list2.append(p)
    p = male.filter(geography="Jiangsu").count()
    list2.append(p)
    p = male.filter(geography="Zhejiang").count()
    list2.append(p)
    p = male.filter(geography="Jiangxi").count()
    list2.append(p)
    p = male.filter(geography="Hubei").count()
    list2.append(p)
    p = male.filter(geography="Guangxi").count()
    list2.append(p)
    p = male.filter(geography="Gansu").count()
    list2.append(p)
    p = male.filter(geography="Shanxi").count()
    list2.append(p)
    p = male.filter(geography="Inner Mongolia").count()
    list2.append(p)
    p = male.filter(geography="Shaanxi").count()
    list2.append(p)
    p = male.filter(geography="Jilin").count()
    list2.append(p)
    p = male.filter(geography="Fujian").count()
    list2.append(p)
    p = male.filter(geography="Guizhou").count()
    list2.append(p)
    p = male.filter(geography="Guangdong").count()
    list2.append(p)
    p = male.filter(geography="Qinghai").count()
    list2.append(p)
    p = male.filter(geography="Tibet").count()
    list2.append(p)
    p = male.filter(geography="Sichuan").count()
    list2.append(p)
    p = male.filter(geography="Ningxia").count()
    list2.append(p)
    p = male.filter(geography="Hainan").count()
    list2.append(p)
    p = male.filter(geography="Taiwan").count()
    list2.append(p)
    p = male.filter(geography="Hong Kong").count()
    list2.append(p)
    p = male.filter(geography="Macao").count()
    list2.append(p)

    context = {"total": total, "female": num_f, "male": num_m, "List1": list1, "List2": list2}
    return render(request, 'APP/geography.html', context)


def age(request): #添加对应的处理方法
    customer = Customer.objects.all()
    female = customer.filter(speaker_sex="female")
    num_f = female.count()
    male = customer.filter(speaker_sex="male")
    num_m = male.count()
    list1 = []
    list2 = []
    age1 = female.filter(speaker_age="<20").count()
    list1.append(age1)
    age2 = female.filter(speaker_age="20-30").count()
    list1.append(age2)
    age3 = female.filter(speaker_age="30-40").count()
    list1.append(age3)
    age4 = female.filter(speaker_age="40-50").count()
    list1.append(age4)
    age5 = female.filter(speaker_age=">50").count()
    list1.append(age5)
    age1 = male.filter(speaker_age="<20").count()
    list2.append(age1)
    age2 = male.filter(speaker_age="20-30").count()
    list2.append(age2)
    age3 = male.filter(speaker_age="30-40").count()
    list2.append(age3)
    age4 = male.filter(speaker_age="40-50").count()
    list2.append(age4)
    age5 = male.filter(speaker_age=">50").count()
    list2.append(age5)
    context = {'female': num_f, 'male': num_m, 'List1': list1, 'List2': list2}
    return render(request, 'APP/age.html', context)


def phone(request): #添加对应的处理方法
    customer = Customer.objects.all()
    list1 = []
    c = customer.filter(phone_type="Huawei").count()
    list1.append(c)
    c = customer.filter(phone_type="Iphone").count()
    list1.append(c)
    c = customer.filter(phone_type="Samsung").count()
    list1.append(c)
    c = customer.filter(phone_type="Oppo").count()
    list1.append(c)
    c = customer.filter(phone_type="Vivo").count()
    list1.append(c)
    c = customer.filter(phone_type="Millet").count()
    list1.append(c)
    c = customer.filter(phone_type="Other").count()
    list1.append(c)
    context = {'List1': list1}
    return render(request, 'APP/phone.html', context)


def environment(request): #添加对应的处理方法
    customer = Customer.objects.all()
    list1 = []
    e = customer.filter(environment="living room").count()
    list1.append(e)
    e = customer.filter(environment="dormitory").count()
    list1.append(e)
    e = customer.filter(environment="bedroom").count()
    list1.append(e)
    e = customer.filter(environment="study").count()
    list1.append(e)
    e = customer.filter(environment="Other").count()
    list1.append(e)
    context = {'List1': list1}
    return render(request, 'APP/environment.html', context)


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
    count = Customer.objects.filter(user=request.user).count()
    if count == 0:
        messages.info(request, "No files uploaded yet!")
    elif count > 5:
        files = Customer.objects.filter(user=request.user)[count-5:] #列表切片，只显示最近上传的五条文件信息
    else:
        files = Customer.objects.filter(user=request.user)
    return render(request, 'APP/file_list.html', {'files': files})


def spectrum_map(request):
    count = Customer.objects.filter(user=request.user).count()
    if count == 0:
        messages.info(request, "No files uploaded yet!")
    else:
        if count > 5:
            files = Customer.objects.filter(user=request.user)[count-5:]
        else:
            files = Customer.objects.filter(user=request.user)
        img = []
        for file in files:
            form = MapForm()
            y, sr = librosa.load(os.path.join(settings.MEDIA_ROOT, file.file.name), sr=None)
            plt.figure()
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            plt.subplot(2, 1, 2)
            librosa.display.specshow(D, y_axis='log')
            plt.colorbar(format='%+2.0f dB')
            plt.title(file.file.name + 'power spectrogram')
            '''将图片以二进制的格式传到前端'''
            buffer = BytesIO()
            plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.2)
            plot_data = buffer.getvalue()
            imb = base64.b64encode(plot_data)  # 对plot_data进行编码
            ims = imb.decode()
            imd = "data:image/png;base64," + ims
            img.append(imd)
            context = {
                'files': files,
                'img': img,
                'form': form,
            }
    return render(request, 'APP/spectrum_map.html', context)


def model(request):
    files = Customer.objects.filter(user=request.user)
    count = Customer.objects.filter(user=request.user).count()
    if count == 0:
        messages.info(request, "No files uploaded yet!")
    return render(request, 'APP/model.html', {'files': files})


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