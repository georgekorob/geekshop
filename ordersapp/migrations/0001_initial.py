# Generated by Django 3.2 on 2021-12-19 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_auto_20211213_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('status', models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PD', 'оплачено'), ('PRD', 'обрабатывается'), ('RDY', 'готов к выдачи'), ('CNC', 'отмена заказа')], default='FM', max_length=3, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='продукты')),
            ],
        ),
    ]
