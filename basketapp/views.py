from django.http import JsonResponse
from django.template.loader import render_to_string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from adminapp.mixins import PageTitleMixin
from basketapp.models import Basket
from mainapp.models import Product


def get_basket_context(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.prod for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    context = {'baskets': baskets,
               'total_sum': total_sum,
               'total_quantity': total_quantity, }
    return context


class BasketCreate(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = Basket
    fields = []
    success_url = reverse_lazy('mainapp:products')

    def form_valid(self, form):
        prod_id = self.kwargs.get('pk')
        req_user = self.request.user
        product = Product.objects.get(id=prod_id)
        baskets = Basket.objects.filter(user=req_user, product=product)
        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=req_user, product=product, quantity=1)
        return JsonResponse({'': ''})


class BasketUpdate(LoginRequiredMixin, PageTitleMixin, UpdateView):
    model = Basket
    fields = []

    def form_valid(self, form):
        qnty = int(form.data.get('qnty'))
        basket = self.get_object()
        if qnty > 0:
            basket.quantity = qnty
            basket.save()
        else:
            basket.delete()
        context = get_basket_context(self.request)
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})


class BasketDelete(LoginRequiredMixin, PageTitleMixin, DeleteView):
    model = Basket

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        context = get_basket_context(request)
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
