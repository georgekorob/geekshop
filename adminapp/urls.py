from django.urls import path
from adminapp.views import index

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
]
