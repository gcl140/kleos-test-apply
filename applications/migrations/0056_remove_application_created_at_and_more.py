# Generated by Django 5.1.5 on 2025-02-05 11:06

import applications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0055_alter_application_adv_school_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='activity',
            name='weeksperyear',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='csee_results',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='financial',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='financial_info_completed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='official_id',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='rec_letter1',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='school_transcripts',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dependent',
            name='dependent_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='relationship',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='distinction',
            name='distinction_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='distinction',
            name='level_of_rec',
            field=models.CharField(blank=True, choices=[('School', 'School'), ('District', 'District'), ('Regional', 'Regional'), ('National', 'National'), ('International', 'International')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='distinction',
            name='year',
            field=models.CharField(blank=True, choices=[('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10'), ('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='sibling',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sibling',
            name='sibling_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
