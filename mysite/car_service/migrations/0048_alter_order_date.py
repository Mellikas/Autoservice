# Generated by Django 4.2.2 on 2023-07-11 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0047_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 10, 58, 40, 450871), verbose_name='date'),
        ),
    ]
