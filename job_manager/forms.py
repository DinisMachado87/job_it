from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = [
            'user', 'is_dream_job', 'slug', 'match_percentage', 'status'
        ]
