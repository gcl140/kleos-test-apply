# Generated by Django 5.1.5 on 2025-03-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0078_application_soc_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='sat_type',
            field=models.CharField(blank=True, choices=[('SAT', 'SAT'), ('SAT Subject', 'SAT Subject'), ('ACT', 'ACT'), ('AP', 'AP'), ('Other', 'Other')], max_length=500, null=True),
        ),
    ]
