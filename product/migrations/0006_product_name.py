# Generated by Django 2.0.2 on 2018-03-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180304_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
    ]
