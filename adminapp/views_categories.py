from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import CategoryCreateForm
from mainapp.models import ProductCategory


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
