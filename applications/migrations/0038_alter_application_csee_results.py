# Generated by Django 5.1.5 on 2025-01-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0037_alter_application_csee_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='csee_results',
            field=models.FileField(blank=True, null=True, upload_to='user_upload_path'),
        ),
    ]
