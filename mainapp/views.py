from django.http import JsonResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.conf import settings
from django.core.cache import cache
from adminapp.mixins import PageTitleMixin
from mainapp.models import ProductCategory, Product


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)


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
        # prods = super().get_queryset()
        prods = get_link_product()
        if cat_id:
            prods = prods.filter(category_id=cat_id)
        self.cat_id = cat_id if cat_id else 0
        return prods

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['sliderphotos'] = [{'alt': 'First', 'img': 'vendor/img/slides/slide-1.jpg'},
                                   {'alt': 'Second', 'img': 'vendor/img/slides/slide-2.jpg'},
                                   {'alt': 'Third', 'img': 'vendor/img/slides/slide-3.jpg'}, ]
        context['categories'] = get_link_category()
        context['cat_id'] = self.cat_id
        context['title'] = 'каталог'
        return context


class ProductDetail(DetailView):
    model = Product


def product_price(request, pk):
    if request.is_ajax():
        product = get_product(pk)
        return JsonResponse({'price': product.price})
