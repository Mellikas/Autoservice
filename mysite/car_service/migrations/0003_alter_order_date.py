# Generated by Django 4.2.2 on 2023-07-03 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0002_remove_order_sum_remove_order_line_t_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 19, 3, 337762), verbose_name='date'),
        ),
    ]