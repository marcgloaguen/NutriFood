# Generated by Django 4.2.3 on 2023-07-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_produit_product_name_fr'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='product_name',
            field=models.CharField(null=True),
        ),
    ]
