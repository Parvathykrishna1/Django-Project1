# Generated by Django 5.0.3 on 2024-03-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('required_qualifications', models.TextField()),
                ('desired_qualifications', models.TextField()),
                ('responsibilities', models.TextField()),
                ('application_deadline', models.DateField()),
                ('salary_range', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('employment_type', models.CharField(max_length=50)),
                ('company_benefits', models.TextField()),
                ('how_to_apply', models.TextField()),
                ('other_information', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('company_location', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('established_year', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
