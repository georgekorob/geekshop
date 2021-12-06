from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductCreateForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


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


class UserList(ListView):
    model = User
    template_name = 'adminapp/users/admin-users-read.html'


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


@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_categories'))
    else:
        form = CategoryCreateForm()
    context = {
        'title': 'Админ | Категория',
        'form': form,
    }
    return render(request, 'adminapp/categories/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def read_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/categories/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update_category(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_categories'))
    else:
        form = CategoryCreateForm(instance=category_select)
    context = {
        'title': 'Админ | Редактирование категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/categories/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, pk):
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.delete()
    return HttpResponseRedirect(reverse('adminapp:read_categories'))


@user_passes_test(lambda u: u.is_superuser)
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_products'))
    else:
        form = ProductCreateForm()
    context = {
        'title': 'Админ | Продукт',
        'form': form,
    }
    return render(request, 'adminapp/products/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def read_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'adminapp/products/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update_product(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_products'))
    else:
        form = ProductCreateForm(instance=product_select)
    context = {
        'title': 'Админ | Редактирование продукта',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/products/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
    return HttpResponseRedirect(reverse('adminapp:read_products'))
