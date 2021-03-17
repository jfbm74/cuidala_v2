from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView, CreateView, FormView, UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Models
from applications.users.models import User, Work, School, Skill


# Forms
from .forms import NewJobForm, NewSchoolForm


# Create your views here.


# Admin site for Patient
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'caregivers/index.html'
    login_url = reverse_lazy('users:login')


# MyProfile

class MyProfileViewList(LoginRequiredMixin, ListView):
    template_name = "caregivers/profile/my_profile.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        current_user = self.request.user
        current_user = User.objects.filter(
            id=current_user.id
        )
        return current_user


class UserUpdateView(UpdateView):
    model = User
    fields = (
        'skills',
        'services',
    )
    template_name = "caregivers/profile/add_skill_service_user.html"


class ProfileViewById(LoginRequiredMixin, ListView):
    template_name = "caregivers/profile/my_profile.html"
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        caregiver_id = self.kwargs['id_user']
        caregiver = User.objects.filter(
            id=caregiver_id
        )
        return caregiver


# Jobs Forms

class NewJobCreateView(LoginRequiredMixin, FormView):
    model = Work
    form_class = NewJobForm
    template_name = 'caregivers/profile/new_job.html'
    success_url = reverse_lazy('caregivers:profile')

    def form_valid(self, form):
        new_work = Work(
            employer=form.cleaned_data['employer'],
            work_title=form.cleaned_data['work_title'],
            start_date=form.cleaned_data['start_date'],
            end_date=form.cleaned_data['end_date'],
            job_description=form.cleaned_data['job_description'],
            location_id=form.cleaned_data['location_id'],
            user_id=self.request.user
        )
        new_work.save()
        return super(NewJobCreateView, self).form_valid(form)


class NewSchoolCreateView(LoginRequiredMixin, FormView):
    model = School
    form_class = NewSchoolForm
    template_name = "caregivers/profile/new_school.html"
    success_url = reverse_lazy('caregivers:profile')

    def form_valid(self, form):
        new_school = School(
            name=form.cleaned_data['name'],
            study=form.cleaned_data['study'],
            start_date=form.cleaned_data['start_date'],
            end_date=form.cleaned_data['end_date'],
            location_id=form.cleaned_data['location_id'],
            user_id=self.request.user
        )
        new_school.save()
        return super(NewSchoolCreateView, self).form_valid(form)


# Job Search Page
class JobSearchView(TemplateView):
    template_name = "caregivers/jobs/job_search.html"
