# Generated by Django 4.2.3 on 2023-07-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_alter_produit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='countries',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.CharField(null=True),
        ),
    ]
