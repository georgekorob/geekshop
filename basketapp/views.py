from django.db import connection
from django.db.models import F
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from adminapp.mixins import PageTitleMixin
from basketapp.models import Basket
from mainapp.models import Product


def db_profile_by_type(instance, query_type, queries):
    update_queries = list(filter(lambda x: query_type in x['sql'], queries))
    print(f'db_profile {query_type} for {instance}:')
    [print(query['sql']) for query in update_queries]


class BasketCreate(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = Basket
    fields = []
    success_url = reverse_lazy('mainapp:products')

    def form_valid(self, form):
        prod_id = self.kwargs.get('pk')
        req_user = self.request.user
        product = Product.objects.get(id=prod_id)
        baskets = req_user.basket.filter(product_id=product.id)
        if baskets:
            basket = baskets.first()
            # basket.quantity += 1
            basket.quantity = F('quantity')+1
            basket.save()
            # db_profile_by_type(basket, 'UPDATE', connection.queries)
        else:
            # Basket.objects.create(user=req_user, product=product, quantity=1)
            Basket.objects.create(user_id=req_user.id, product_id=product.id, quantity=1)
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
        # result = render_to_string('basketapp/basket.html', self.request.user.get_baskets)
        result = render_to_string('basketapp/basket.html', {'user': self.request.user})
        return JsonResponse({'result': result})


class BasketDelete(LoginRequiredMixin, PageTitleMixin, DeleteView):
    model = Basket

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        # result = render_to_string('basketapp/basket.html', self.request.user.get_baskets)
        result = render_to_string('basketapp/basket.html', {'user': self.request.user})
        return JsonResponse({'result': result})
