from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    age = models.PositiveIntegerField(default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True, null=True)

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True

    @property
    def get_baskets(self):
        from basketapp.models import Basket
        baskets = Basket.objects.select_related().filter(user_id=self.id)
        total_sum = sum(basket.prod for basket in baskets)
        total_quantity = sum(basket.quantity for basket in baskets)
        return {
            'baskets': baskets,
            'total_sum': total_sum,
            'total_quantity': total_quantity,
        }


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='о себе', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, blank=True, max_length=2)
    langs = models.CharField(verbose_name='язык', blank=True, max_length=10, default='RU')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.username}'

    class Meta:
        verbose_name = 'пользователь vk'
        verbose_name_plural = 'пользователи vk'
