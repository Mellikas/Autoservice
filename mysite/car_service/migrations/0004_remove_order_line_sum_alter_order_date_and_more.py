# Generated by Django 4.2.2 on 2023-07-03 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0003_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_line',
            name='sum',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 26, 17, 69077), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(auto_created=True, default=0, max_length=10000, primary_key=True, serialize=False),
        ),
    ]
