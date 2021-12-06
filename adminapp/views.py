from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductCreateForm
from adminapp.mixins import SuperUserOnlyMixin, PageTitleMixin
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


class UserCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = User
    form_class = UserAdminRegisterForm
    page_title = 'админ: создание пользователя'
    success_url = reverse_lazy('adminapp:read_users')


class UserListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = User
    page_title = 'админ: все пользователи'


class UserUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'authapp/user_update_delete.html'
    page_title = 'админ: редактирование пользователя'
    success_url = reverse_lazy('adminapp:read_users')


class UserDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'authapp/user_update_delete.html'
    page_title = 'админ: удалить пользователя'
    success_url = reverse_lazy('adminapp:read_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    page_title = 'админ: создание категории'
    success_url = reverse_lazy('adminapp:read_categories')


class CategoryListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ProductCategory
    page_title = 'админ: все категории'


class CategoryUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'mainapp/productcategory_update_delete.html'
    page_title = 'админ: редактирование категории'
    success_url = reverse_lazy('adminapp:read_categories')


class CategoryDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'mainapp/productcategory_update_delete.html'
    page_title = 'админ: удалить категорию'
    success_url = reverse_lazy('adminapp:read_categories')


class ProductCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    page_title = 'админ: создание продукта'
    success_url = reverse_lazy('adminapp:read_products')


class ProductListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = Product
    page_title = 'админ: все продукты'


class ProductUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'mainapp/product_update_delete.html'
    page_title = 'админ: редактирование продукта'
    success_url = reverse_lazy('adminapp:read_products')


class ProductDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'mainapp/product_update_delete.html'
    page_title = 'админ: удалить продукт'
    success_url = reverse_lazy('adminapp:read_products')
