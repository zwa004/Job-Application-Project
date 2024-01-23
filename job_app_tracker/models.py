from django.db import models

# Create model for form collecting Job Title, Company, Date Applied, Application URL, Salary Range, Experience Level and Job Description
class JobApp(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_applied = models.DateField()
    application_url = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    job_description = models.CharField(max_length=2000)
    SALARY_CHOICES = [
        ('<30000', 'Less than $30,000'),
    ('30000-50000', '$30,000 - $50,000'),
    ('50001-70000', '$50,001 - $70,000'),
    ('70001-90000', '$70,001 - $90,000'),
    ('90001-110000', '$90,001 - $110,000'),
    ('110001-130000', '$110,001 - $130,000'),
    ('130001-150000', '$130,001 - $150,000'),
    ('>150000', 'More than $150,000'),
    ]
    salary_range = models.CharField(max_length=20, choices=SALARY_CHOICES)

    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
    ('entry', 'Entry Level'),
    ('mid', 'Mid Level'),
    ('senior', 'Senior Level'),
    ('manager', 'Manager'),
    ('director', 'Director'),
    ('executive', 'Executive'),
    ]
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)

    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
    ('finance', 'Finance'),
    ('healthcare', 'Healthcare'),
    ('education', 'Education'),
    ('manufacturing', 'Manufacturing'),
    ('retail', 'Retail'),
    ('hospitality', 'Hospitality'),
    ('government', 'Government'),
    ('nonprofit', 'Non-Profit'),
    ]
    industry = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)

    # Create string representation of data collected
    def __str__(self):
        return self.title