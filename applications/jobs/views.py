from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    FormView,
)
from django.http import HttpResponseRedirect
# URL's Helpers
from django.urls import reverse_lazy, reverse
# Models
from .models import Jobs, Applicants
from applications.users.models import User


# Create your views here.


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


def job_apply(request, id):
    job = Jobs.objects.filter(
        id=id
    ).first()
    print(job.salary_min)
    Applicants.objects.create(
        job_id=job,
        caregiver_id=request.user,
        patient_offer=job.salary_min,
        caregiver_offer=job.salary_min,
    )
    return HttpResponseRedirect(reverse('jobs:search_jobs'))


def inactivate_job(request, id):
    job = Jobs.objects.filter(
        id=id
    ).first()
    job.status = '0'
    job.save()
    return HttpResponseRedirect(reverse('jobs:my_inactive_jobs'))


def inactivate_applicant(id_applicant):
    candidate = Applicants.objects.filter(
        id=id_applicant,
    ).first()
    candidate.status = '0'
    candidate.save()
    return candidate


def inactivate_applicant_process(request, id_applicant):
    application = inactivate_applicant(id_applicant)
    return HttpResponseRedirect(reverse('patients:list_candidates', kwargs={'id_job': application.job_id}))


def hire_applicant(id_applicant):
    candidate = Applicants.objects.filter(
        id=id_applicant,
    ).first()
    candidate.status = '2'
    candidate.save()
    return candidate


def job_status_hired(job_id):
    # Changing Job Offer Status to Hired
    actual_job_offer = Jobs.objects.filter(
        id=job_id
    ).first()
    print(actual_job_offer.status)
    actual_job_offer.status = '2'
    print(actual_job_offer.status)
    actual_job_offer.save()
    return actual_job_offer


def hiring_process(request, id_applicant):
    # Hiring a Caregiver Process
    contacted_user = hire_applicant(id_applicant)
    # Inactivating other caregiver's applicants process
    applicants = Applicants.objects.filter(
        job_id=contacted_user.job_id,
        status=1
    )
    for a in applicants:
        inactivate_applicant(a.id)

    # Changing Job Offer Status to Hired
    job_status_hired(contacted_user.job_id.id)
    return HttpResponseRedirect(reverse('patients:list_candidates', kwargs={'id_job': contacted_user.job_id.id}))
