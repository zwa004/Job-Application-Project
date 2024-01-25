from django.db import models

# Create model for form collecting Job Title, Company, Date Applied, Application URL, Salary Range, Experience Level, Job Description, etc
class JobApp(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_applied = models.DateField()
    application_url = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    job_description = models.CharField(max_length=2000)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    SALARY_CHOICES = [
        ('<30000', 'Less than $30,000'),
        ('30000-35000', '$30,000 - $35,000'),
        ('35000-40000', '$35,000 - $40,000'),
        ('40000-45000', '$40,000 - $45,000'),
        ('45000-50000', '$45,000 - $50,000'),
        ('50000-55000', '$50,000 - $55,000'),
        ('55000-60000', '$55,000 - $60,000'),
        ('60000-65000', '$60,000 - $65,000'),
        ('65000-70000', '$65,000 - $70,000'),
        ('70000-75000', '$70,000 - $75,000'),
        ('75000-80000', '$75,000 - $80,000'),
        ('80000-85000', '$80,000 - $85,000'),
        ('85000-90000', '$85,000 - $90,000'),
        ('90000-95000', '$90,000 - $95,000'),
        ('95000-100000', '$95,000 - $100,000'),
        ('100000-105000', '$100,000 - $105,000'),
        ('105000-110000', '$105,000 - $110,000'),
        ('110000-115000', '$110,000 - $115,000'),
        ('115000-120000', '$115,000 - $120,000'),
        ('120000-125000', '$120,000 - $125,000'),
        ('125000-130000', '$125,000 - $130,000'),
        ('130000-135000', '$130,000 - $135,000'),
        ('135000-140000', '$135,000 - $140,000'),
        ('140000-145000', '$140,000 - $145,000'),
        ('145000-150000', '$145,000 - $150,000'),
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