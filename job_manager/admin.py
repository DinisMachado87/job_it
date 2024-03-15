from django.contrib import admin
from .models import Job
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    '''
    Job admin class to register the Job model
    - define the fields to be displayed in the admin panel
    - define the job description field to be used for searching
    - define the fields to be used for filtering
    - define the prepopulating reference for the slug field
    '''
    list_display = (
        'user',
        'job_to_apply',
        'pay',
        'status',
        'freelance_hire',
        'responsibility',
        'schedule_type',
        'company_size',
        'office_type'
        )
    search_fields = ['job_description']
    list_filter = (
        'user',
        'freelance_hire',
        'responsibility',
        'schedule_type',
        'company_size',
        'bring_pet',
        'own_computer',
        'office_type',
        'pet_sitter',
        'child_care',
        'status'
        )
    prepopulated_fields = {'slug': ('job_to_apply', 'employer'), }
