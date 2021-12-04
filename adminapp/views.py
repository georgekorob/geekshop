from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm
from authapp.models import User


def index(request):
    return render(request, 'adminapp/admin.html')


def create_user(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() #fdkebov427hflk
            return HttpResponseRedirect(reverse('adminapp:read_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админ | Регистрация',
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html',context)


def read_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


def update_user(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


def delete_user(request):
    return render(request, 'adminapp/admin-users-read.html')
