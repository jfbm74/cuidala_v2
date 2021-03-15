from django.contrib import admin
from .models import (
    User,
    Location,
    Skill,
    Service,
    School,
    Work
)

# Register your models here.

admin.site.register(Location)
admin.site.register(Skill)
admin.site.register(Service)


# Presentation in django admin panel
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'legal_id',
        'email',
        'caregiver',
        'patient',
        'location_id',
    )
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('patient', 'skills')
    filter_horizontal = ('skills',)


admin.site.register(User, UserAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'study',
        'start_date',
        'end_date',
        'location_id',
        'user_id',
    )
    search_fields = ('study',)
    list_filter = ('study', 'location_id',)
    # filter_horizontal = ('care_category', 'service_category',)


admin.site.register(School, SchoolAdmin)


class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employer',
        'work_title',
        'start_date',
        'end_date',
        'job_description',
        'location_id',
        'user_id',
    )
    search_fields = ('user_id',)
    list_filter = ('work_title', 'location_id',)


admin.site.register(Work, WorkAdmin)

