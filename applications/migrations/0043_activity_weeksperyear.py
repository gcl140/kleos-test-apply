# Generated by Django 5.1.5 on 2025-01-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0042_application_files_signature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='weeksperyear',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
