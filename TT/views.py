from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from . import models
from django.urls import reverse_lazy


class Listviews(ListView):
    context_object_name = 'tables'
    model = models.timetable
    template_name = 'TT/list.html'


class TTDetailView(DetailView):
    context_object_name = 'TT_detail'
    model = models.timetable
    template_name = 'TT/timetable_detail.html'


class TTCreate(CreateView):
    fields = ('days', 'sub1','sub2','sub3','sub4','sub6','sub7','sub8')
    model = models.timetable
    success_url = reverse_lazy("TT:list")


class TTUpdate(UpdateView):
    fields = ('sub1','sub2','sub3','sub4','sub6','sub7','sub8')
    model = models.timetable
    success_url = reverse_lazy("TT:list")


class TTDelete(DeleteView):
    model = models.timetable
    success_url = reverse_lazy("TT:list")