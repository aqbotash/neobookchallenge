# Generated by Django 5.0 on 2023-12-13 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoMarketAPI', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecoMarketAPI.product'),
        ),
    ]
