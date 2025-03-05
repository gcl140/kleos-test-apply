# Generated by Django 5.1.5 on 2025-01-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_rename_name_dependent_dependent_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='place_of_birth',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='organization_name',
            field=models.CharField(blank=True, max_length=2555, null=True),
        ),
    ]
