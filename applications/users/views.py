from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from django.views.generic.edit import (
    View,
    FormView,
)
from django.http import HttpResponseRedirect
from .models import User
from .forms import PatientRegisterForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class LoginUser(FormView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('patients:home')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users:login'
            )
        )


class PatientRegisterCreateView(FormView):
    template_name = "home/register_patient.html"
    form_class = PatientRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            legal_id=form.cleaned_data['legal_id'],
            gender=form.cleaned_data['gender'],
            phone=form.cleaned_data['phone'],

        )
        return super(PatientRegisterCreateView, self).form_valid(form)


class ListAllUsersListView(ListView):
    """
    List all Users in Cuidala
    """
    model = User
    paginate_by = 4
    template_name = "users/list_all_users.html"


class ListAllPatientsListView(ListView):
    """
    List All Patients in Cuidala
    """
    template_name = "users/patients/list_all_patients.html"
    queryset = User.objects.filter(
        patient=True
    )


class ListPatientsByLocationListView(ListView):
    """List all patients by location given by URL"""
    template_name = "users/patients/list_patients_location.html"

    def get_queryset(self):
        city = self.kwargs['city']
        listing = User.objects.filter(
            patient=True,
            location_id__name=city,
        )
        return listing


class ListPatientByKwordListView(ListView):
    """
    List Patient by Service / Diseases Keyword
    """
    template_name = "users/patients/services_by_kword.html"
    context_object_name = "patients"

    def get_queryset(self):
        service = self.request.GET.get('kword', )
        listing = User.objects.filter(
            patient=True,
            skills__name=service
        )
        return listing


class PatientDetailsListView(ListView):
    """
    Lists a given Patient
    """
    template_name = "users/patients/patient_details.html"

    def get_queryset(self):
        id_patient = self.kwargs['id']
        patient_details = User.objects.filter(
            id=id_patient,
        )
        return patient_details


class ListAllCaregiversListView(ListView):
    """ List all caregivers """
    template_name = "users/caregivers/list_all_caregivers.html"
    queryset = User.objects.filter(
        caregiver=True
    )
