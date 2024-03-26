# Generated by Django 5.0.3 on 2024-03-26 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CareerForge', '0001_initial'),
        ('TalentHub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='job_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TalentHub.joblisting'),
        ),
    ]