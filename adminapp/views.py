from django.shortcuts import render


# Create your views here.
from authapp.models import User


def index(request):
    return render(request, 'adminapp/admin.html')


def create_user(request):
    return render(request, 'adminapp/admin-users-create.html')


def read_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


def update_user(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


def delete_user(request):
    return render(request, 'adminapp/admin-users-read.html')
