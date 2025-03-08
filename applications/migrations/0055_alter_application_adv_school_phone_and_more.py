# Generated by Django 5.1.5 on 2025-02-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0054_application_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='adv_school_phone',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='application',
            name='olv_school_phone',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='application',
            name='other_adv_school_phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='other_olv_school_phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='par1_phone',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='application',
            name='par2_phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='tel1',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='application',
            name='tel2',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]
