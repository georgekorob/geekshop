from django.contrib.auth.decorators import user_passes_test
from django.db import connection
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductCreateForm, \
    ProductUpdateForm, CategoryUpdateForm
from adminapp.mixins import SuperUserOnlyMixin, PageTitleMixin
from authapp.models import User
from basketapp.views import db_profile_by_type
from mainapp.models import ProductCategory, Product


class IndexTemplateView(SuperUserOnlyMixin, PageTitleMixin, TemplateView):
    template_name = 'adminapp/admin.html'
    title = 'админка'


class UserCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = User
    form_class = UserAdminRegisterForm
    title = 'админ: создание пользователя'
    success_url = reverse_lazy('adminapp:read_users')


class UserListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = User
    title = 'админ: все пользователи'


class UserUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'authapp/user_update_delete.html'
    title = 'админ: редактирование пользователя'
    success_url = reverse_lazy('adminapp:read_users')


class UserDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'authapp/user_update_delete.html'
    title = 'админ: удалить пользователя'
    success_url = reverse_lazy('adminapp:read_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    title = 'админ: создание категории'
    success_url = reverse_lazy('adminapp:read_categories')


class CategoryListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ProductCategory
    title = 'админ: все категории'


class CategoryUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    form_class = CategoryUpdateForm
    template_name = 'mainapp/productcategory_update_delete.html'
    title = 'админ: редактирование категории'
    success_url = reverse_lazy('adminapp:read_categories')

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(price=F('price') * (1 - discount / 100))
                # db_profile_by_type(self.model, 'UPDATE', connection.queries)
                # Пример вывода:
                # db_profile UPDATE for <class 'mainapp.models.ProductCategory'>:
                # UPDATE "mainapp_product" SET "price" = ("mainapp_product"."price" * 0.9) WHERE "mainapp_product"."category_id" = 4
        return super().form_valid(form)


class CategoryDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    template_name = 'mainapp/productcategory_update_delete.html'
    success_url = reverse_lazy('adminapp:read_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        activate = not self.object.is_active
        self.object.product_set.update(is_active=activate)
        self.object.is_active = activate
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    title = 'админ: создание продукта'
    success_url = reverse_lazy('adminapp:read_products')


class ProductListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = Product
    title = 'админ: все продукты'


class ProductUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'mainapp/product_update_delete.html'
    title = 'админ: редактирование продукта'
    success_url = reverse_lazy('adminapp:read_products')


class ProductDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = Product
    template_name = 'mainapp/product_update_delete.html'
    success_url = reverse_lazy('adminapp:read_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
