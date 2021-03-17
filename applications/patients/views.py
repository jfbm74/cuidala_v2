from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.jobs.models import Applicants, Jobs
# Create your views here.


# Admin site for Patient
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "patients/index.html"
    login_url = reverse_lazy('users:login')


class ListCandidatesByJob(LoginRequiredMixin, ListView):
    template_name = "patients/candidates/applicants.html"
    login_url = reverse_lazy('users:login')
    context_object_name = 'applicants'

    def get_queryset(self):
        job = self.kwargs['id_job']
        listing = Applicants.objects.filter(
            job_id=job,
        )
        return listing
