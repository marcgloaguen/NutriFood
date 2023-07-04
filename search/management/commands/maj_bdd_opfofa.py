from django.core.management.base import BaseCommand
import requests
import json
from NutriFood.search.models import produit
class Command(BaseCommand):
    help = 'Récupérer les produits par catégories'

    def add_arguments(self, parser):
        parser.add_argument('Categories', nargs='+', type=str)
        parser.add_argument('Maximum de produits', type=int, default=100)

    def handle(self, *args, **options):
        categories = options['Categories']
        max_products = options['Maximum de produits']
        for categorie in categories:
            url = f"https://world.openfoodfacts.org/category/{categorie}/{max_products}.json"
            response = requests.get(url)
            if response.status_code == 200:
                products = json.loads(response.text)['products']
                for product in products:
                    brand = product['brands']
                    nutrition_grade = product['nutrition_grade_fr']
                    product_obj = produit(brand=brand, nutrition_grade=nutrition_grade)
                    product_obj.save()