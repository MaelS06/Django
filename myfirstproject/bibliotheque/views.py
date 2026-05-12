from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    return render(request,"bibliotheque/ajout.html",{"form" : LivreForm()}) # envoie vers une page d'ajout de Livre avec un formulaire vierge

def traitement(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request.POST)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/affiche.html",{"Livre" : Livre}) # envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        return render(request,"bibliotheque/ajout.html",{"form" : LivreForm()})

# PAGE D'ACCUEIL
def index(request):
    liste = list(models.Livre.objects.all())

    return render(request, 'bibliotheque/index.html', {
        'liste': liste
    })

def read(request, id):
    livre = models.Livre.objects.get(pk=id)

    return render(request, 'bibliotheque/affiche.html', {
        'Livre': livre
    })

def update(request, id):
    livre = models.Livre.objects.get(pk=id)

    dico = {
        'titre': livre.titre,
        'auteur': livre.auteur,
        'date_parution': livre.date_parution,
        'nombre_pages': livre.nombre_pages,
        'resume': livre.resume
    }

    form = LivreForm(dico)

    return render(request, 'bibliotheque/update.html', {
        'form': form,
        'id': id
    })

def traitementupdate(request, id):
    livre = models.Livre.objects.get(pk=id)

    form = LivreForm(request.POST)

    if form.is_valid():
        livre.titre = form.cleaned_data['titre']
        livre.auteur = form.cleaned_data['auteur']
        livre.date_parution = form.cleaned_data['date_parution']
        livre.nombre_pages = form.cleaned_data['nombre_pages']
        livre.resume = form.cleaned_data['resume']

        livre.save()

        return render(request, 'bibliotheque/affiche.html', {
            'Livre': livre
        })
    else:
        return render(request, 'bibliotheque/update.html', {
            'form': form,
            'id': id
        })

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)

    livre.delete()

    return index(request)