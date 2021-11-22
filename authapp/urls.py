from django.urls import path
<<<<<<< HEAD
from authapp.views import login, register, logout

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
=======
# from authapp.views import User

app_name = 'authapp'
urlpatterns = [
#    path('', User, name='authapp'),
>>>>>>> 02ad150... create authapp, user model
]
