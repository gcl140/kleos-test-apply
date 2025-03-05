# Generated by Django 5.1.5 on 2025-03-04 13:39

import applications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0080_alter_application_sat_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='csee_results',
            new_name='a_level_school_transcripts',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ib_scores',
            new_name='adv_certificates',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='school_transcripts',
            new_name='o_level_school_transcripts',
        ),
        migrations.AddField(
            model_name='application',
            name='olv_certificates',
            field=models.FileField(default=1, upload_to=applications.models.user_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='eng_type',
            field=models.CharField(blank=True, choices=[('TOEFL', 'TOEFL'), ('IELTS', 'IELTS'), ('Duolingo', 'Duolingo'), ('Other', 'Other')], max_length=500, null=True),
        ),
    ]
