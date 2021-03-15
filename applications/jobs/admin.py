from django.contrib import admin

# Register your models here.


# Presentation in django admin panel
class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
        'user_id',
        'location_id',
        'salary_min',
        'salary_max',
    )
    search_fields = ('email', 'first_name', 'last_name', )
    list_filter = ('status', 'location_id', )
    filter_horizontal = ('care_category', 'service_category',)



