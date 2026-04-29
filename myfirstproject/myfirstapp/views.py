from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myfirstapp/index.html")

def formulaire(request):
    return render(request, "myfirstapp/formulaire.html")

def bonjour(request):
    prenom = request.GET.get("prenom")
    nom = request.GET.get("nom")
    return render(request, "myfirstapp/bonjour.html", {"prenom": prenom, "nom": nom})
