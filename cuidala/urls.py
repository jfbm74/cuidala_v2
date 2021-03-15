"""Cuidala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, re_path, include
from applications.home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    re_path('home/', include('applications.home.urls')),
    re_path('users/', include('applications.users.urls')),
    re_path('patients/', include('applications.patients.urls')),
    re_path('caregivers/', include('applications.caregivers.urls')),
    re_path('jobs/', include('applications.jobs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
