# Generated by Django 5.0.3 on 2024-03-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_remove_customuser_confirm_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('job_seeker', 'Job Seeker'), ('employer_recruiter', 'Employer/Recruiter')], max_length=20),
        ),
    ]