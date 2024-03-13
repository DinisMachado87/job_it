from django.contrib import admin
from .models import Job
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# admin.site.register(Job)
@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = ('job_to_apply', 'pay', 'status', 'freelance_hire', 'responsibility', 'schedule_type', 'company_size', 'office_type')
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
    prepopulated_fields = {'slug': ('job_to_apply','employer'),}