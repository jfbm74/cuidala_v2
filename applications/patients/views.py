from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


# Admin site for Patient
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "patients/index.html"
    login_url = reverse_lazy('users:login')
