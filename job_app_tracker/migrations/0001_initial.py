# Generated by Django 4.1 on 2024-01-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobApp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("company", models.CharField(max_length=200)),
                ("date_applied", models.DateField()),
                ("application_url", models.CharField(max_length=200)),
                ("salary_range", models.CharField(max_length=200)),
                ("experience_level", models.CharField(max_length=200)),
                ("job_description", models.CharField(max_length=2000)),
            ],
        ),
    ]
