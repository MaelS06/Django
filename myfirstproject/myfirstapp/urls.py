from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('formulaire/', views.index2),
]
