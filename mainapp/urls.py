from django.urls import path
from mainapp.views import index, products

app_name = 'products'
urlpatterns = [
    path('', products, name='products'),
]
