from django.urls import path
from adminapp.views import index, create_user, read_users, update_user, delete_user

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('create_user', create_user, name='create_user'),
    path('read_users', read_users, name='read_users'),
    path('update_user/<int:pk>', update_user, name='update_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
]
