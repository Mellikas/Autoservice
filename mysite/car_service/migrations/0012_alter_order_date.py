# Generated by Django 4.2.2 on 2023-07-03 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0011_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 14, 21, 38, 942728), verbose_name='date'),
        ),
    ]
