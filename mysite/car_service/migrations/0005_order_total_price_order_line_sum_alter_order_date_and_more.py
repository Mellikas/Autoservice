# Generated by Django 4.2.2 on 2023-07-03 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0004_remove_order_line_sum_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='total_price'),
        ),
        migrations.AddField(
            model_name='order_line',
            name='sum',
            field=models.FloatField(default=0, verbose_name='t_price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 41, 5, 957170), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]