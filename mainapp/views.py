from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {'title': 'каталог', 'sliderphotos': [
        {'alt': 'First', 'img': 'vendor/img/slides/slide-1.jpg'},
        {'alt': 'Second', 'img': 'vendor/img/slides/slide-2.jpg'},
        {'alt': 'Third', 'img': 'vendor/img/slides/slide-3.jpg'},
    ], 'categories': ProductCategory.objects.all()}
    if pk:
        context['products'] = Product.objects.filter(category_id=pk)
    else:
        context['products'] = Product.objects.all()
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