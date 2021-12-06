from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from mainapp.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        'page_title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


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
        context['page_title'] = 'каталог'
        return context


class ProductDetail(DetailView):
    model = Product
