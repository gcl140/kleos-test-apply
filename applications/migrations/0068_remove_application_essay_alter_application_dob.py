# Generated by Django 5.1.5 on 2025-02-06 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0067_alter_application_dob_alter_application_eng_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='essay',
        ),
        migrations.AlterField(
            model_name='application',
            name='dob',
            field=models.DateField(default=datetime.date(2025, 1, 1)),
        ),
    ]
