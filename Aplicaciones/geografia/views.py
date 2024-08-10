from django.shortcuts import render
from django.http import JsonResponse
from .models import Pais, Ciudad

# Create your views here.
def index(request):
    return render(request,'index.html')

def listarPaises(request):
    paises= list(Pais.objects.values())
    
    if(len(paises)>0):
        data={'message':"Se Logro",'paises':paises}
    else:
        data={'message':"No Funciono"}
    return JsonResponse(data)

def listarCiudades(request, pais_id):
    ciudades=list(Ciudad.objects.filter(pais_id = pais_id).values())
    if(len(ciudades)>0):
        data={'message': "Se logro", 'ciudades':ciudades}
    else:
        data={'message':"no hay datos"}
    return JsonResponse(data)