from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.mixins import PageTitleMixin
from basketapp.models import Basket
from ordersapp.forms import OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrderList(PageTitleMixin, ListView):
    model = Order
    title = 'список заказов'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)


class OrderCreate(PageTitleMixin, CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'создание заказа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = order_form_set(self.request.POST)
        else:
            basket_item = Basket.objects.filter(user=self.request.user)
            if basket_item:
                order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=basket_item.count())
                formset = order_form_set()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                basket_item.delete()
            else:
                formset = order_form_set()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super().form_valid(form)


class OrderUpdate(PageTitleMixin, UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'обновление заказа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = order_form_set(self.request.POST, instance=self.object)
        else:
            formset = order_form_set(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super().form_valid(form)


class OrderDelete(PageTitleMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'удаление заказа'


class OrderDetail(PageTitleMixin, DetailView):
    model = Order
    title = 'просмотр заказа'


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))
