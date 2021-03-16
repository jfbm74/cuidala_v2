from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import request
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
)
# URL's Helpers
from django.urls import reverse_lazy
# Models
from .models import Jobs
from .managers import JobsManager

# Create your views here.


# Jobs
from ..users.models import Work


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


class ListActiveJobs(LoginRequiredMixin, ListView):
    context_object_name = 'jobs'
    template_name = "caregivers/jobs/job_search.html"

    def get_queryset(self):
        return Jobs.objects.list_active_jobs()


class ListActiveJobsByLocation(LoginRequiredMixin, ListView):
    """List all Jobs by location given by URL"""
    context_object_name = 'posts'
    template_name = "caregivers/jobs/job_search_city.html"

    def get_queryset(self):
        city = self.kwargs['city']
        return Jobs.objects.list_active_jobs_by_url(city)
