from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import request
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
)
from django.views.generic.edit import (
    FormView,
)
from django.urls import reverse_lazy
from .models import Jobs

# Create your views here.


# Jobs
class MyActiveJobsView(LoginRequiredMixin, ListView):
    """Listing Active Jobs for current Patient"""
    template_name = "patients/jobs/my_active_jobs.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        current_user = self.request.user
        listing = Jobs.objects.filter(
            status='1',
            user_id=current_user.id
        )
        return listing


class MyInactiveJobsView(LoginRequiredMixin, ListView):
    """Listing Active Jobs for current Patient"""
    template_name = "patients/jobs/my_inactive_jobs.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        current_user = self.request.user
        listing = Jobs.objects.filter(
            status='0',
            user_id=current_user.id
        )
        return listing

class MyHiredJobsView(LoginRequiredMixin, ListView):
    """Listing Active Jobs for current Patient"""
    template_name = "patients/jobs/my_hired_jobs.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        current_user = self.request.user
        listing = Jobs.objects.filter(
            status='2',
            user_id=current_user.id
        )
        return listing

# Create Jobs


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = (
        'description',
        'recipient_care',
        'user_id',
        'location_id',
        'care_category',
        'service_category'

    )
    template_name = "patients/jobs/create_job.html"
    success_url = reverse_lazy('patients:home')
    login_url = reverse_lazy('users:login')
