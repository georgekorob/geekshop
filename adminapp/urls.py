from django.urls import path
from adminapp.views import index, create_user, read_users, update_user, delete_user
from adminapp.views import create_category, read_categories, update_category, delete_category

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('create_user', create_user, name='create_user'),
    path('read_users', read_users, name='read_users'),
    path('update_user/<int:pk>', update_user, name='update_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('create_category', create_category, name='create_category'),
    path('read_categories', read_categories, name='read_categories'),
    path('update_category/<int:pk>', update_category, name='update_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
]
