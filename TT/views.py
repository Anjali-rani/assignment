from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . import models
from django.urls import reverse_lazy


class CreateTimeTable(TemplateView):
    template_name = 'TT/createTT.html'


class FillTimeTable(TemplateView):
    template_name = 'TT/FillTT.html'
