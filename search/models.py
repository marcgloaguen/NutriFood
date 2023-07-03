from django.db import models


class produit(models.Model):
    ingredient = models.CharField(max_length=100 ,null=True)