from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from authapp.models import User


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админ | Регистрация',
        'form': form,
    }
    return render(request, 'adminapp/users/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def read_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/users/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update_user(request, pk):
    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админ | Редактирование пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/users/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = not user.is_active
        user.save()
    return HttpResponseRedirect(reverse('adminapp:read_users'))

