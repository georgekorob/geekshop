from django.http import HttpResponseRedirect
from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product


# Create your views here.


def basket_add(request, id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select, product=product)
    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    pass
