# Generated by Django 5.1.5 on 2025-01-19 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0030_rename_level_distinction_level_of_rec_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='eng_date',
            field=models.DateField(blank=True, default=datetime.date(2000, 1, 1), null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='eng_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='eng_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sat_date',
            field=models.DateField(blank=True, default=datetime.date(2000, 1, 1), null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sat_for_eng',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='sat_for_sat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='sat_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sat_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
