from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from basketapp.models import Basket
from ordersapp.models import OrderItem


# Метод с BasketQuerySet и переопределение save и delete предпочтительнее
@receiver(pre_save, sender=Basket)
@receiver(pre_save, sender=OrderItem)
def product_quantity_update_save(sender, instance, **kwargs):
    if instance.pk:
        get_item = instance.get_item(int(instance.pk))
        instance.product.quantity -= instance.quantity - get_item
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=Basket)
@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.save()
