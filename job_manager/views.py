from django.shortcuts import render
from django.views import generic
from .models import Job

# Create your views here.
class JobListView(generic.ListView):
    queryset = Job.objects.all()
    template_name = 'job_list.html'
