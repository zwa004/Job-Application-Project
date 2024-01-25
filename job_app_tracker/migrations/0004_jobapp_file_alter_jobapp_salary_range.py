# Generated by Django 4.1 on 2024-01-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_app_tracker", "0003_jobapp_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobapp",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AlterField(
            model_name="jobapp",
            name="salary_range",
            field=models.CharField(
                choices=[
                    ("<30000", "Less than $30,000"),
                    ("30000-35000", "$30,000 - $35,000"),
                    ("35000-40000", "$35,000 - $40,000"),
                    ("40000-45000", "$40,000 - $45,000"),
                    ("45000-50000", "$45,000 - $50,000"),
                    ("50000-55000", "$50,000 - $55,000"),
                    ("55000-60000", "$55,000 - $60,000"),
                    ("60000-65000", "$60,000 - $65,000"),
                    ("65000-70000", "$65,000 - $70,000"),
                    ("70000-75000", "$70,000 - $75,000"),
                    ("75000-80000", "$75,000 - $80,000"),
                    ("80000-85000", "$80,000 - $85,000"),
                    ("85000-90000", "$85,000 - $90,000"),
                    ("90000-95000", "$90,000 - $95,000"),
                    ("95000-100000", "$95,000 - $100,000"),
                    ("100000-105000", "$100,000 - $105,000"),
                    ("105000-110000", "$105,000 - $110,000"),
                    ("110000-115000", "$110,000 - $115,000"),
                    ("115000-120000", "$115,000 - $120,000"),
                    ("120000-125000", "$120,000 - $125,000"),
                    ("125000-130000", "$125,000 - $130,000"),
                    ("130000-135000", "$130,000 - $135,000"),
                    ("135000-140000", "$135,000 - $140,000"),
                    ("140000-145000", "$140,000 - $145,000"),
                    ("145000-150000", "$145,000 - $150,000"),
                    (">150000", "More than $150,000"),
                ],
                max_length=20,
            ),
        ),
    ]
