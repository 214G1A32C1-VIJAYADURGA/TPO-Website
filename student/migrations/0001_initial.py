# Generated by Django 5.1.6 on 2025-03-04 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentRegistration",
            fields=[
                (
                    "rollno",
                    models.CharField(
                        max_length=20, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("full_name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="student.studentregistration",
                    ),
                ),
                ("college_email", models.EmailField(max_length=254, unique=True)),
                (
                    "personal_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "ssc_percentage",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "inter_diploma_percentage",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "btech_cgpa",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                ("department", models.CharField(max_length=100)),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="resumes/"),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pictures/"
                    ),
                ),
                ("is_placed", models.BooleanField(default=False)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("F", "Female"), ("M", "Male"), ("O", "Others")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("passed_out_year", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
