from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myfirstapp/index.html")

def formulaire(request):
    return render(request, "myfirstapp/formulaire.html")

def bonjour(request):
    nom = request.GET["nom"]
    return render(request, 'myfirstapp/bonjour.html', {"nom": nom})

def heritant(request):
    return render(request, "myfirstapp/heritant.html")
