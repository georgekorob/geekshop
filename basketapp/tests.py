from django.test import TestCase
from django.test.client import Client
from basketapp.models import Basket


# Create your tests here.
from mainapp.models import Product


class TestSmokeBasket(TestCase):
    fixtures = ['authapp.json', 'mainapp.json', 'basketapp.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_basket_prod(self):
        basket_1 = Basket.objects.first()
        self.assertEqual(basket_1.prod, basket_1.product.price*basket_1.quantity)

    def test_basket_del(self):
        basket = Basket.objects.first()
        product = Product.objects.get(id=basket.product_id)
        basket_quantity = basket.quantity
        product_quantity = product.quantity
        basket.delete()
        self.assertEqual(Product.objects.get(id=basket.product_id).quantity, product_quantity+basket_quantity)
