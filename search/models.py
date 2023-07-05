from django.db import models


class Produit(models.Model):
    id = models.CharField(primary_key=True)
    tag = models.CharField(null=True)
    brands = models.TextField(null=True)
    nutrition_grade_fr = models.CharField(null=True)
    countries = models.CharField(null=True)

