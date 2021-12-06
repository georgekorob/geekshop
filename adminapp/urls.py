from django.urls import path
from adminapp.views import index, UserCreateView, UserListView, update_user, delete_user, create_category, read_categories, \
    update_category, delete_category, create_product, read_products, update_product, delete_product

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('create_user', UserCreateView.as_view(), name='create_user'),
    path('read_users', UserListView.as_view(), name='read_users'),
    path('update_user/<int:pk>', update_user, name='update_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('create_category', create_category, name='create_category'),
    path('read_categories', read_categories, name='read_categories'),
    path('update_category/<int:pk>', update_category, name='update_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
    path('create_product', create_product, name='create_product'),
    path('read_products', read_products, name='read_products'),
    path('update_product/<int:pk>', update_product, name='update_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
]
