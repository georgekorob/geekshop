from django.urls import path
from basketapp.views import basket_add, BasketDelete, basket_edit

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:id>/', basket_add, name='basket_add'),
    path('remove/<int:pk>/', BasketDelete.as_view(), name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
