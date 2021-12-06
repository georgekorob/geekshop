from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    context = {'title': 'каталог', 'sliderphotos': [
        {'alt': 'First', 'img': 'vendor/img/slides/slide-1.jpg'},
        {'alt': 'Second', 'img': 'vendor/img/slides/slide-2.jpg'},
        {'alt': 'Third', 'img': 'vendor/img/slides/slide-3.jpg'},
    ], 'categories': ProductCategory.objects.all()}

    if pk:
        prods = Product.objects.filter(category_id=pk)
    else:
        prods = Product.objects.all()

    paginator = Paginator(prods, per_page=2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator

    return render(request, 'mainapp/products.html', context)


def detail(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'mainapp/detail.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context