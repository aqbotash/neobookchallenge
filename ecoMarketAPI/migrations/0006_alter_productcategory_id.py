# Generated by Django 5.0 on 2023-12-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoMarketAPI', '0005_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
