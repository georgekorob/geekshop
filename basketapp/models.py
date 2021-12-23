from django.db import models

# Create your models here.
from authapp.models import User
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super().delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user.username} | Продукт {self.product.name}'

    @property
    def prod(self):
        return self.quantity * self.product.price

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.save()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.get_item(int(self.pk))
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
