from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from django.contrib.auth.mixins import LoginRequiredMixin
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

        cat_id = int(request.GET.get('cat_id', 0))
        if cat_id:
            products = Product.objects.filter(category=cat_id)
        else:
            products = Product.objects.all()
        paginator = Paginator(products, 3)
        page = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context = {'page_obj': page_obj, }
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
        total_sum = sum(basket.prod for basket in baskets)
        total_quantity = sum(basket.quantity for basket in baskets)
        context = {'baskets': baskets,
                   'total_sum': total_sum,
                   'total_quantity': total_quantity, }
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
