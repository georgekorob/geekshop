from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product


# Create your views here.
@login_required
def basket_add(request, id):
    if request.is_ajax():
        user_select = request.user
        product = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=user_select, product=product)
        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user_select, product=product, quantity=1)

        products = Product.objects.all()
        context = {'products': products, }
        result = render_to_string('mainapp/includes/card.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        total_sum = sum(basket.sum for basket in baskets)
        total_quantity = sum(basket.quantity for basket in baskets)
        context = {'baskets': baskets,
                   'total_sum': total_sum,
                   'total_quantity': total_quantity, }
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})

# @login_required
# def basket_add(request, id):
#     user_select = request.user
#     product = Product.objects.get(id=id)
#     baskets = Basket.objects.filter(user=user_select, product=product)
#     if baskets:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#     else:
#         Basket.objects.create(user=user_select, product=product, quantity=1)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
