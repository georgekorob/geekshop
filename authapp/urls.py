from django.urls import path
from authapp.views import UserLoginView, UserRegisterView, UserLogoutView, UserProfileView

app_name = 'authapp'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activate_key>/', UserRegisterView.verify, name='verify'),
]
