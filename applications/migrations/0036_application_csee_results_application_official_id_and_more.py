# Generated by Django 5.1.5 on 2025-01-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0035_alter_application_known_tansaf_other_write'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='csee_results',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='application',
            name='official_id',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='application',
            name='school_transcripts',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='application',
            name='supps',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
