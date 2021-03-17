"""cuidala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"


urlpatterns = [
    # Register Patient
    path('register-patient/',
         views.PatientRegisterCreateView.as_view(),
         name='register_patient',),
    path('register-caregiver/',
         views.CaregiverRegisterCreateView.as_view(),
         name='register_caregiver', ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='logout'
    ),
    path('list-users/', views.ListAllUsersListView.as_view()),

    # Patients URL's
    path('list-patients/', views.ListAllPatientsListView.as_view()),
    path('list-patients-locations/<city>', views.ListPatientsByLocationListView.as_view()),
    path('search-patients-services/', views.ListPatientByKwordListView.as_view()),
    path('patient-details/<id>', views.PatientDetailsListView.as_view()),

    # Caregivers Url's
    path('list-caregivers/', views.ListAllCaregiversListView.as_view()),

]
