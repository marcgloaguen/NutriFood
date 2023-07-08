from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Produit

def index(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")

def id(request, id):
    object = Produit.objects.get(id=id)
    context = {'brands': object.brands}

    return render(request, 'search/id_infos.html', context)