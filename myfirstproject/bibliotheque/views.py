from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/affiche.html",{"Livre" : Livre}) # envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"bibliotheque/ajout.html",{"form" : form})