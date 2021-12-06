from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductCreateForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_key = 'page_title'
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.page_key] = self.page_title
        return context


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


@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_categories'))
    else:
        form = CategoryCreateForm()
    context = {
        'title': 'Админ | Категория',
        'form': form,
    }
    return render(request, 'adminapp/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def read_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update_category(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_categories'))
    else:
        form = CategoryCreateForm(instance=category_select)
    context = {
        'title': 'Админ | Редактирование категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, pk):
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.delete()
    return HttpResponseRedirect(reverse('adminapp:read_categories'))


@user_passes_test(lambda u: u.is_superuser)
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_products'))
    else:
        form = ProductCreateForm()
    context = {
        'title': 'Админ | Продукт',
        'form': form,
    }
    return render(request, 'adminapp/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def read_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'adminapp/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update_product(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:read_products'))
    else:
        form = ProductCreateForm(instance=product_select)
    context = {
        'title': 'Админ | Редактирование продукта',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
    return HttpResponseRedirect(reverse('adminapp:read_products'))
