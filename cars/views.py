from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import Engine, Dye, Wheels, Car


class CarCreate(CreateView):
    pass


class CarUpdate(UpdateView):
    pass


class CarDetail(DetailView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        return context


class CarList(ListView):
    model = Car
    context_object_name = 'car_list'
