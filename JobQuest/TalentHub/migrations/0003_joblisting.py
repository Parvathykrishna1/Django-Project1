# Generated by Django 5.0.3 on 2024-03-24 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TalentHub', '0002_rename_recruiterupdateprofile_recruiterprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
