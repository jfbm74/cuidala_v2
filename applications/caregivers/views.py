from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Models
from applications.users.models import User


# Create your views here.


# Admin site for Patient
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "caregivers/index.html"
    login_url = reverse_lazy('users:login')


# MyProfile

class MyProfileViewList(LoginRequiredMixin, ListView):
    template_name = "caregivers/my_profile.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        current_user = self.request.user
        current_user = User.objects.filter(
            id=current_user.id
        )
        return current_user