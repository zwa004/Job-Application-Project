from django.db import models

# Create model for form collecting Job Title, Company, Date Applied, Application URL, Salary Range, Experience Level and Job Description
class JobApp(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_applied = models.DateField()
    application_url = models.CharField(max_length=200)
    salary_range = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    job_description = models.CharField(max_length=2000)

    # Create string representation of data collected
    def __str__(self):
        return self.title