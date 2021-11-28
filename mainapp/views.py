from django.shortcuts import render
from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'каталог', 'sliderphotos': [
        {'alt': 'First', 'img': 'vendor/img/slides/slide-1.jpg'},
        {'alt': 'Second', 'img': 'vendor/img/slides/slide-2.jpg'},
        {'alt': 'Third', 'img': 'vendor/img/slides/slide-3.jpg'},
    ], 'categories': ProductCategory.objects.all(), 'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def detail(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'mainapp/detail.html', context)
