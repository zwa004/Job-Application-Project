from django import forms
from .models import JobApp
from django.forms.widgets import DateInput

class JobAppForm(forms.ModelForm):
    date_applied = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JobApp
        fields = ['title', 'company', 'date_applied', 'application_url', 'salary_range', 'experience_level', 'industry','status','employment_type','job_description', 'resume', 'cover_letter']
