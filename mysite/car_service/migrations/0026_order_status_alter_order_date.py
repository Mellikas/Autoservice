# Generated by Django 4.2.2 on 2023-07-05 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0025_alter_order_date_alter_orderline_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Accepted'), ('p', 'In progress'), ('c', 'Completed')], default='a', help_text='Order status', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 10, 22, 4, 395936), verbose_name='date'),
        ),
    ]
