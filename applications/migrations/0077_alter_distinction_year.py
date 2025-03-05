# Generated by Django 5.1.5 on 2025-03-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0076_alter_activity_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distinction',
            name='year',
            field=models.CharField(blank=True, choices=[('Grade 9', 'Grade 9/ Form 3'), ('Grade 10', 'Grade 10/ Form 4'), ('Grade 11', 'Grade 11/ Form 5'), ('Grade 12', 'Grade 12/ Form 6')], max_length=500, null=True),
        ),
    ]
