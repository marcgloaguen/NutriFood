from django.db import models


class Produit(models.Model):
    id = models.CharField(primary_key=True)
    brands = models.TextField(null=True)
    nutrition_grade_fr = models.CharField(null=True)
