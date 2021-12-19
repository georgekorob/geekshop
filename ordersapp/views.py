# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.mixins import PageTitleMixin


class OrderList(ListView, PageTitleMixin):
    pass


class OrderCreate(CreateView, PageTitleMixin):
    pass


class OrderUpdate(UpdateView):
    pass


class OrderDelete(DeleteView, PageTitleMixin):
    pass


class OrderDetail(DetailView, PageTitleMixin):
    pass


def order_forming_complete(request, pk):
    pass
