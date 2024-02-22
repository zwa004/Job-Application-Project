from django.db import models

# Create model for form collecting Job Title, Company, Date Applied, Application URL, Salary Range, Experience Level, Job Description, etc
class JobApp(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_applied = models.DateField()
    last_modified = models.DateTimeField(auto_now=True)
    application_url = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    job_description = models.CharField(max_length=2000, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]

    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    # Change salary range to open text field
    salary_range = models.CharField(max_length=200)
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

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interviewed', 'Interviewed'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Accepted Offer'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
        ('no_response', 'No Response'),
        ('awaiting_decision', 'Awaiting Decision'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')

    # Create string representation of data collected
    def __str__(self):
        return self.title