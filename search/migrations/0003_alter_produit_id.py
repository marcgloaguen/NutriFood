# Generated by Django 4.2.3 on 2023-07-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_alter_produit_brands_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]
