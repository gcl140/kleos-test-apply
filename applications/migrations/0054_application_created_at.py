# Generated by Django 5.1.5 on 2025-01-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0053_application_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
