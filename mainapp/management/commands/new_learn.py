from django.core.management.base import BaseCommand
from prettytable import PrettyTable

from ordersapp.models import OrderItem
from mainapp.models import Product

from django.db.models import F, When, Case, DecimalField, IntegerField, Q
from datetime import timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
        ACTION_1 = 1
        ACTION_2 = 2
        ACTION_EXPIRED = 3

        action_1__time_delta = timedelta(minutes=20)  # hours=12
        action_2__time_delta = timedelta(hours=1)  # days=1

        action_1__discount = 0.3
        action_2__discount = 0.15
        action_expired__discount = 0.05

        action_1__condition = Q(order__updated__lte=F('order__created') + action_1__time_delta)

        action_2__condition = Q(order__updated__gt=F('order__created') + action_1__time_delta) & \
                              Q(order__updated__lte=F('order__created') + action_2__time_delta)

        action_expired__condition = Q(order__updated__gt=F('order__created') + action_2__time_delta)

        action_1__order = When(action_1__condition, then=ACTION_1)
        action_2__order = When(action_2__condition, then=ACTION_2)
        action_expired__order = When(action_expired__condition, then=ACTION_EXPIRED)

        action_1__profit = When(action_1__condition, then=F('product__price') * F('quantity') * action_1__discount)

        action_2__profit = When(action_2__condition, then=F('product__price') * F('quantity') * -action_2__discount)

        action_expired__profit = When(action_expired__condition,
                                     then=F('product__price') * F('quantity') * action_expired__discount)

        test_orderss = OrderItem.objects.filter(order__is_active=True).annotate(
            action_order=Case(
                action_1__order,
                action_2__order,
                action_expired__order,
                output_field=IntegerField(),
            )).annotate(
            total_profit=Case(
                action_1__profit,
                action_2__profit,
                action_expired__profit,
                output_field=DecimalField(),
            )).order_by('action_order', 'total_profit').select_related()

        t_list = PrettyTable(["Заказ", "Товар", "Скидка", 'Разница времени'])
        t_list.align = 'l'
        for orderitem in test_orderss:
            t_list.add_row([f'{orderitem.action_order} заказ №{orderitem.order.pk:}', f'{orderitem.product.name}',
                            f'{abs(orderitem.total_profit):6.2f} руб.',
                            orderitem.order.updated - orderitem.order.created])
        print(t_list)

# +-------------+-------------------------------------------------+-------------+------------------------+
# | Заказ       | Товар                                           | Скидка      | Разница времени        |
# +-------------+-------------------------------------------------+-------------+------------------------+
# | 1 заказ №12 | Темно-синие широкие строгие брюки ASOS DESIGN   | 867.00 руб. | 0:00:23.477976         |
# | 2 заказ №11 | Черный рюкзак Nike Heritage                     | 351.00 руб. | 0:22:59.709932         |
# | 3 заказ №1  | Черный рюкзак Nike Heritage                     | 117.00 руб. | 3 days, 2:20:32.959743 |
# | 3 заказ №1  | Темно-синие широкие строгие брюки ASOS DESIGN   | 144.50 руб. | 3 days, 2:20:32.959743 |
# | 3 заказ №1  | Коричневый спортивный oversized-топ ASOS DESIGN | 169.50 руб. | 3 days, 2:20:32.959743 |
# +-------------+-------------------------------------------------+-------------+------------------------+
