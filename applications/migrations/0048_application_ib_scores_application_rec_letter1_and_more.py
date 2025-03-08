# Generated by Django 5.1.5 on 2025-01-24 09:18

import applications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0047_application_financial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='ib_scores',
            field=models.FileField(blank=True, null=True, upload_to=applications.models.user_upload_path),
        ),
        migrations.AddField(
            model_name='application',
            name='rec_letter1',
            field=models.FileField(blank=True, null=True, upload_to=applications.models.user_upload_path),
        ),
        migrations.AddField(
            model_name='application',
            name='rec_letter2',
            field=models.FileField(blank=True, null=True, upload_to=applications.models.user_upload_path),
        ),
    ]
