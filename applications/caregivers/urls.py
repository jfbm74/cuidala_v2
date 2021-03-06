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

app_name = "caregivers"

urlpatterns = [
    path(
        'home/',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'my-profile/',
        views.MyProfileViewList.as_view(),
        name='profile'
    ),
    path(
        'caregiver-profile/<id_user>',
        views.ProfileViewById.as_view(),
        name='caregiver_profile'
    ),
    path(
        'new-job/',
        views.NewJobCreateView.as_view(),
        name='new_job'
    ),
    path(
        'new-school/',
        views.NewSchoolCreateView.as_view(),
        name='new_school'
    ),
    path(
        'new-skill/',
        views.NewSchoolCreateView.as_view(),
        name='new_skill'
    ),
    path(
        'update-user/<pk>',
        views.UserUpdateView.as_view(),
        name='update_user'
    ),
]