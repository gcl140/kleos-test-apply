# Generated by Django 5.1.5 on 2025-01-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0027_activity_activity_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='outside_school',
            field=models.BooleanField(default=False),
        ),
    ]
