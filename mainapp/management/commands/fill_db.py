import json
from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            _category = category.get('fields')
            _category['id'] = category.get('pk')
            new_category = ProductCategory(**_category)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            _product = product.get('fields')
            category = _product.get('category')
            category = ProductCategory.objects.get(id=category)
            _product['category'] = category
            new_product = Product(**_product)
            new_product.save()

        users = load_from_json('users.json')

        User.objects.all().delete()
        for user in users:
            _user = user.get('fields')
            _user['id'] = user.get('pk')
            new_user = User(**_user)
            new_user.save()

