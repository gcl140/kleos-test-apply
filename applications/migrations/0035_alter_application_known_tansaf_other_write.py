# Generated by Django 5.1.5 on 2025-01-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0034_application_known_tansaf_other_write'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='known_tansaf_other_write',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
