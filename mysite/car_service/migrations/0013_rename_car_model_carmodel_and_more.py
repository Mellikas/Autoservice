# Generated by Django 4.2.2 on 2023-07-04 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0012_alter_order_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car_model',
            new_name='CarModel',
        ),
        migrations.RenameModel(
            old_name='Order_line',
            new_name='OrderLine',
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Make', 'verbose_name_plural': 'Makes'},
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 9, 57, 37, 46705), verbose_name='date'),
        ),
    ]
