# Generated by Django 4.2.2 on 2023-07-04 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0016_alter_order_date_alter_orderline_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 11, 0, 50, 65948), verbose_name='date'),
        ),
    ]
