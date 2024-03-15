from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    '''
    Job form class that defines the form fields
    to add a new job to apply based on the Job model
    '''
    class Meta:
        model = Job
        fields = '__all__'
