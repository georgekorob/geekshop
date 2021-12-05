from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import ProductCreateForm
from mainapp.models import Product


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
