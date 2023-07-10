from django.db import models


class Produit(models.Model):
    id = models.CharField(primary_key=True)
    brands = models.TextField(null=True)
    nutrition_grade_fr = models.CharField(null=True)
    countries = models.CharField(null=True)
    product_name_fr = models.CharField(null=True)
    product_name = models.CharField(null=True)
    pnns_groups_1 = models.CharField(null=True)

