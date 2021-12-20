from django.urls import path
from basketapp.views import BasketCreate, BasketDelete, BasketUpdate

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:pk>/', BasketCreate.as_view(), name='basket_add'),
    path('remove/<int:pk>/', BasketDelete.as_view(), name='basket_remove'),
    path('edit/<int:pk>/', BasketUpdate.as_view(), name='basket_edit'),
]
