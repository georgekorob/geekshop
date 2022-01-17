from django.test import TestCase
from django.urls import reverse

from mainapp.models import ProductCategory, Product
from django.test.client import Client


class TestSmokeMain(TestCase):
    # Smoke test - проверить, но не изменять
    # Case test - проверить с изменением базы
    # python manage.py test mainapp.tests.TestMainSmokeTest
    # pip install win-unicode-console
    fixtures = ['mainapp.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    # def setUp(self):
    #     category = ProductCategory.objects.create(
    #         name='TestCat1'
    #     )
    #     Product.objects.create(
    #         category=category,
    #         name='product_test_1',
    #         image='product_image/product_default.png',
    #         price=100
    #     )
    #     self.client = Client()
    # def tearDown(self):
    # call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')
    # определяется для очистки после
    # работы теста исполяется после setUP
    # (базу удалять не нужно она автоматом удалится)
    # но данные чистим допустим когда мы выкачивали
    # аватар на первом уроке ее можно почистить
    # но очень редко сам использую и коллеги тоже
    # pass

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_categories_page(self):
        for category in ProductCategory.objects.all():
            response = self.client.get(reverse('mainapp:category', kwargs={'cat_id': category.pk, 'page': 1}))
            self.assertEqual(response.status_code, 200)

    def test_products_detail(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="стулья")
        self.product_1 = Product.objects.create(name="стул 1", category=category, price=1999.5, quantity=150)
        self.product_2 = Product.objects.create(name="стул 2", category=category, price=998.1, quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="стул 1")
        product_2 = Product.objects.get(name="стул 2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)
