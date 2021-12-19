from django.contrib import admin

# Register your models here.
from authapp.models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
