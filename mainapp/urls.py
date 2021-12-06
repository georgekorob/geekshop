from django.urls import path
from mainapp.views import ProductList, ProductDetail

app_name = 'mainapp'
urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('category/<int:cat_id>/page/<int:page>/', ProductList.as_view(), name='category'),
    path('page/<int:page>/', ProductList.as_view(), name='page'),

    # path('detail/<int:id>/', detail, name='detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]
