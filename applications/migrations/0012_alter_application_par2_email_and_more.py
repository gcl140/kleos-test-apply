# Generated by Django 5.1.4 on 2025-01-06 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0011_application_signed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='par2_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_fname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_jobbusy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_levedu',
            field=models.CharField(choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('HighSchool', 'High School or Vocational training education'), ('BachelorDeg', 'Bachelors degree or equivalent level'), ('MastersDeg', 'Masters degree or equivalent level'), ('PhD', 'PhD')], default='PhD', max_length=255),
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_lname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_retire',
            field=models.DateField(blank=True, default=datetime.date(2000, 1, 1), null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_served',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
