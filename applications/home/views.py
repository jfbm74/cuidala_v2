from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import (
    TemplateView,
)

# Create your views here.
from applications.home.models import Prueba


class HomeView(TemplateView):
    """Shows Cuidala's Home Page"""
    template_name = "home/index.html"


class RegisterUsers(TemplateView):
    template_name = "home/register_patient.html"
