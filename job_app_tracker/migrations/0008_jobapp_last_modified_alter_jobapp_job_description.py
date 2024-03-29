# Generated by Django 4.1 on 2024-02-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_app_tracker", "0007_alter_jobapp_salary_range"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobapp",
            name="last_modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="jobapp",
            name="job_description",
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
