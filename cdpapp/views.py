from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Building, Unit, WorkOrder


class BuildingList(ListView):
    model = Building
    template_name = 'cdpapp/index.html'
    context_object_name = 'buildings'


class BuildingDetail(DetailView):
    model = Building
    template_name = 'cdpapp/building_detail.html'
    context_object_name = 'buildings_detail'


class BuildingUnitDetail(DetailView):
    model = Unit
    template_name = 'cdpapp/building_units_detail.html'
    context_object_name = 'units'
