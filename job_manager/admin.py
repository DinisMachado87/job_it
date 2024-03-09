from django.contrib import admin
from .models import Job
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# admin.site.register(Job)
@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = ('job_description', 'slug', 'status')
    search_fields = ('job_description',)
    list_filter = ('freelance_hire', 'responsibility')
    summernote_fields = ('job_description')
    prepopulated_fields = {'slug': ('job_to_apply',)}

