from django.core.management.base import BaseCommand
from django.db import connection

from basketapp.views import db_profile_by_type
from mainapp.models import Product
from django.db.models import Q, F


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(
            # Q(category__name='Обувь') | Q(category__name='Одежда'))
            # <QuerySet [<Product: Темно-синие широкие строгие брюки ASOS DESIGN>, <Product: Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex>, <Product: Синяя куртка The North Face>]>
            # db_profile  for learn db:
            # SELECT "mainapp_product"."id", "mainapp_product"."name", "mainapp_product"."image",
            # "mainapp_product"."description", "mainapp_product"."price", "mainapp_product"."quantity",
            # "mainapp_product"."category_id", "mainapp_product"."is_active"
            # FROM "mainapp_product"
            # INNER JOIN "mainapp_productcategory"
            # ON ("mainapp_product"."category_id" = "mainapp_productcategory"."id")
            # WHERE ("mainapp_productcategory"."name" = 'Обувь' OR "mainapp_productcategory"."name" = 'Одежда')
            # ORDER BY "mainapp_product"."price" ASC LIMIT 21

            # Q(category__name='Одежда') & Q(price__lt=10000))
            # <QuerySet [<Product: Темно-синие широкие строгие брюки ASOS DESIGN>]>
            # db_profile  for learn db:
            # SELECT "mainapp_product"."id", "mainapp_product"."name", "mainapp_product"."image",
            # "mainapp_product"."description", "mainapp_product"."price", "mainapp_product"."quantity",
            # "mainapp_product"."category_id", "mainapp_product"."is_active"
            # FROM "mainapp_product"
            # INNER JOIN "mainapp_productcategory"
            # ON ("mainapp_product"."category_id" = "mainapp_productcategory"."id")
            # WHERE ("mainapp_productcategory"."name" = 'Одежда' AND "mainapp_product"."price" < '10000')
            # ORDER BY "mainapp_product"."price" ASC LIMIT 21

            Q(category__name='Одежда') & Q(price__gt=10000))
            # <QuerySet [<Product: Синяя куртка The North Face>]>
            # db_profile  for learn db:
            # SELECT "mainapp_product"."id", "mainapp_product"."name", "mainapp_product"."image",
            # "mainapp_product"."description", "mainapp_product"."price", "mainapp_product"."quantity",
            # "mainapp_product"."category_id", "mainapp_product"."is_active"
            # FROM "mainapp_product"
            # INNER JOIN "mainapp_productcategory"
            # ON ("mainapp_product"."category_id" = "mainapp_productcategory"."id")
            # WHERE ("mainapp_productcategory"."name" = 'Одежда' AND "mainapp_product"."price" > '10000')
            # ORDER BY "mainapp_product"."price" ASC LIMIT 21
        print(products)
        db_profile_by_type('learn db', '', connection.queries)
