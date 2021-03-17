from django.contrib import admin
from .models import Jobs, Applicants


# Register your models here.


# Presentation in django admin panel
class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'status',
        'user_id',
        'location_id',
        'salary_min',
        'salary_max',
    )
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('status', 'location_id',)
    filter_horizontal = ('care_category', 'service_category',)


admin.site.register(Jobs, JobsAdmin)


class ApplicantsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'job_id',
        'caregiver_offer',
        'patient_offer',
        'status',
        'caregiver_id',
    )
    search_fields = ('status', 'caregiver_id',)
    list_filter = ('status', 'caregiver_id',)
    # filter_horizontal = ('care_category', 'service_category',)


admin.site.register(Applicants, ApplicantsAdmin)
