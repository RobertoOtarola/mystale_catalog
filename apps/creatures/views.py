from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Creature
from .forms import CreatureForm


class CreatureListView(ListView):
    model = Creature
    template_name = 'creatures/creature_list.html'
    context_object_name = 'creatures'

    def get_queryset(self):
        qs = super().get_queryset()
        element = self.request.GET.get('element')
        if element:
            qs = qs.filter(element_type=element)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['element_choices'] = Creature.ELEMENT_CHOICES
        ctx['selected_element'] = self.request.GET.get('element', '')
        return ctx
