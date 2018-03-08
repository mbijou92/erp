# Generated by Django 2.0.2 on 2018-03-08 05:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20180308_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 8, 5, 49, 35, 679215, tzinfo=utc), verbose_name='Erstellt'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Bearbeitet'),
        ),
    ]