# Generated by Django 2.0.2 on 2018-03-08 06:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20180308_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 8, 6, 2, 11, 716588, tzinfo=utc), verbose_name='Erstellt'),
        ),
    ]
