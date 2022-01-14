from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.mixins import PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ordersapp.forms import OrderItemsForm
from ordersapp.models import Order, OrderItem
# from ordersapp.signals import product_quantity_update_delete, product_quantity_update_save


class OrderList(LoginRequiredMixin, PageTitleMixin, ListView):
    model = Order
    title = 'список заказов'

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id, is_active=True)


class OrderCreate(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:list')
    title = 'создание заказа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update(self.request.user.get_baskets)

        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = order_form_set(self.request.POST)
        else:
            # basket_item = context.get('baskets')
            basket_item = self.request.user.get_baskets.get('baskets')
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

            if self.object.get_summary().get('get_total_cost') == 0:
                self.object.delete()
        return super().form_valid(form)


class OrderUpdate(LoginRequiredMixin, PageTitleMixin, UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:list')
    title = 'обновление заказа'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        queryset = self.object.orderitems.select_related()
        if self.request.POST:
            formset = order_form_set(self.request.POST, instance=self.object, queryset=queryset)
        else:
            formset = order_form_set(instance=self.object, queryset=queryset)
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

            if self.object.get_summary().get('get_total_cost') == 0:
                self.object.delete()
        return super().form_valid(form)


class OrderDelete(LoginRequiredMixin, PageTitleMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:list')
    title = 'удаление заказа'


class OrderDetail(LoginRequiredMixin, PageTitleMixin, DetailView):
    model = Order
    title = 'просмотр заказа'


@login_required
def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('ordersapp:list'))
