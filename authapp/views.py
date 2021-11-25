from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm


# Create your views here.
from basketapp.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'реддактирование',
               'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               }
    return render(request, 'authapp/profile.html', context)
