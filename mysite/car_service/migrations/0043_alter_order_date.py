# Generated by Django 4.2.2 on 2023-07-10 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0042_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 11, 31, 16, 818391), verbose_name='date'),
        ),
    ]