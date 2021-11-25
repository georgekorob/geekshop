from django.urls import path
from basketapp.views import basket_add, basket_remove

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:id>/', basket_add, name='basket_add'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
]
