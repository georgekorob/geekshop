from django.urls import path
from mainapp.views import products, detail, ProductDetail

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
    path('category/<int:pk>/', products, name='category'),

    # path('detail/<int:id>/', detail, name='detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]
