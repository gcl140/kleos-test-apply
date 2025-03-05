# Generated by Django 5.1.3 on 2025-01-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuzzaz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinator',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='combination',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='curriculum',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='f4_necta_grades',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='f6_necta_grades',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='former_school',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='intended_major',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='main_teacher_email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='main_teacher_phone',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='parents_email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='parents_phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='coordinator',
            name='username',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
