# Generated by Django 4.2.20 on 2025-03-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuzzaz', '0003_customuser_is_intern_delete_coordinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_intern',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
