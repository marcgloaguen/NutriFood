from django.db import models


class produit(models.Model):
    produits = models.CharField(max_length=100 ,null=True) #brands
    nutrition_grade_fr = models.CharField(max_length=100, null=True) #nutrition_grade_fr
