# Generated by Django 4.2.2 on 2023-07-14 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0063_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 13, 37, 19, 301979), verbose_name='date'),
        ),
    ]
