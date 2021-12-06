from django.urls import path
from mainapp.views import products, ProductDetail

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
    path('category/<int:pk>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),

    # path('detail/<int:id>/', detail, name='detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]
