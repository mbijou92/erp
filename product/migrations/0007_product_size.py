# Generated by Django 2.0.2 on 2018-03-04 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Größe'),
        ),
    ]
