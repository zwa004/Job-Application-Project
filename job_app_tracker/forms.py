from django import forms
from .models import JobApp

class JobAppForm(forms.ModelForm):
    class Meta:
        model = JobApp
        fields = ['title', 'company', 'date_applied', 'application_url', 'salary_range', 'experience_level', 'industry','status','job_description']
