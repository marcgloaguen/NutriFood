from django.core.management.base import BaseCommand
import requests
import json
from search.models import Produit


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
                    _id = product.get('_id')
                    brands = product.get('brands')
                    nutrition_grade_fr = product.get('nutrition_grade_fr')
                    countries = product.get('countries')

                    product_obj = Produit(
                        id=_id,
                        brands=brands,
                        nutrition_grade_fr=nutrition_grade_fr,
                        countries=countries,
                        tag=categories[0]
                    )
                    product_obj.save()
