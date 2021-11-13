from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)
