# Generated by Django 4.2.2 on 2023-07-12 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0049_order_client_order_due_back_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 9, 53, 27, 98144), verbose_name='date'),
        ),
    ]
