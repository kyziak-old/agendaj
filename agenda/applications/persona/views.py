# Django
from django.shortcuts import render
from django.views.generic import ListView

# Models
from .models import Person

class PersonaListView(ListView):
    """ Listar personas view """
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self): 
        return Person.objects.all()

