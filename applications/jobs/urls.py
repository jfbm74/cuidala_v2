
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

app_name = "jobs"


urlpatterns = [
    path(
        'my-active-jobs/',
        views.MyActiveJobsView.as_view(),
        name='my_active_jobs'
    ),
    path(
        'my-inactive-jobs/',
        views.MyInactiveJobsView.as_view(),
        name='my_inactive_jobs'
    ),
    path(
        'my-hired-jobs/',
        views.MyHiredJobsView.as_view(),
        name='my_hired_jobs'
    ),
    path(
        'create/',
        views.JobCreateView.as_view(),
        name='create_job'
    ),
]
