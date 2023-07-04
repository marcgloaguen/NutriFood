from django.db import models


class Produit(models.Model):
    id = models.IntegerField(max_length=100, null=False)
    brands = models.CharField(max_length=100, null=True)
    nutrition_grade_fr = models.CharField(max_length=100, null=True)
