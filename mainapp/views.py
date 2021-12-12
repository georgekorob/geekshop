from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from adminapp.mixins import PageTitleMixin
from mainapp.models import ProductCategory, Product


# Create your views here.
class IndexTemplateView(PageTitleMixin, TemplateView):
    template_name = 'mainapp/index.html'
    title = 'магазин'


class ProductList(ListView):
    model = Product
    paginate_by = 3
    template_name = 'mainapp/products.html'

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        prods = super().get_queryset()
        if cat_id:
            prods = prods.filter(category_id=cat_id)
        self.cat_id = cat_id if cat_id else 0
        return prods

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['sliderphotos'] = [{'alt': 'First', 'img': 'vendor/img/slides/slide-1.jpg'},
                                   {'alt': 'Second', 'img': 'vendor/img/slides/slide-2.jpg'},
                                   {'alt': 'Third', 'img': 'vendor/img/slides/slide-3.jpg'}, ]
        context['categories'] = ProductCategory.objects.all()
        context['cat_id'] = self.cat_id
        context['title'] = 'каталог'
        return context


class ProductDetail(DetailView):
    model = Product
