# Generated by Django 5.1.5 on 2025-01-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0049_alter_application_eng_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sibling',
            name='education',
            field=models.CharField(choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('High School', 'High School or Vocational training education'), ('Bachelor degree', 'Bachelors degree or equivalent level'), ('Masters', 'Masters degree or equivalent level'), ('PhD', 'PhD')], default='PhD', max_length=500),
        ),
    ]
