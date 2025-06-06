# Generated by Django 4.2.20 on 2025-03-29 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_intern', '0004_sibling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distinction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distinction_name', models.CharField(blank=True, max_length=500, null=True)),
                ('level_of_rec', models.CharField(blank=True, choices=[('School', 'School'), ('District', 'District'), ('Regional', 'Regional'), ('National', 'National'), ('International', 'International')], max_length=500, null=True)),
                ('year', models.CharField(blank=True, choices=[('Grade 9', 'Grade 9/ Form 3'), ('Grade 10', 'Grade 10/ Form 4'), ('Grade 11', 'Grade 11/ Form 5'), ('Grade 12', 'Grade 12/ Form 6')], max_length=500, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_intern_distinctions', to='application_intern.applicationintern')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('Academic', 'Academic'), ('Art', 'Art'), ('Athletics', 'Athletics'), ('Community Service', 'Community Service'), ('Computer/Technology', 'Computer/Technology'), ('Cultural', 'Cultural'), ('Dance', 'Dance'), ('Debate/Speech', 'Debate/Speech'), ('Environmental', 'Environmental'), ('Family Responsibilities', 'Family Responsibilities'), ('Foreign Exchange', 'Foreign Exchange'), ('Foreign Language', 'Foreign Language'), ('Journalism', 'Journalism'), ('Music: Instrumental', 'Music: Instrumental'), ('Music: Vocal', 'Music: Vocal'), ('Religious', 'Religious'), ('Research', 'Research'), ('Robotics', 'Robotics'), ('School spirit', 'School spirit'), ('Robotics', 'Robotics'), ('Science/Math', 'Science/Math'), ('Social Justice', 'Social Justice'), ('Student Govt./Politics', 'Student Govt./Politics'), ('Theatre/Drama', 'Theatre/Drama'), ('Work(Paid)', 'Work(Paid)'), ('Other Club/Activity', 'Other Club/Activity')], max_length=500)),
                ('leadership_position', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=5005, null=True)),
                ('weeksperyear', models.PositiveIntegerField(blank=True, null=True)),
                ('hoursperweek', models.PositiveIntegerField(blank=True, null=True)),
                ('activity_description', models.TextField(blank=True, null=True)),
                ('outside_school', models.BooleanField(default=False)),
                ('start_year', models.CharField(blank=True, choices=[('Grade 9', 'Grade 9/ Form 3'), ('Grade 10', 'Grade 10/ Form 4'), ('Grade 11', 'Grade 11/ Form 5'), ('Grade 12', 'Grade 12/ Form 6')], max_length=500, null=True)),
                ('end_year', models.CharField(blank=True, choices=[('Grade 9', 'Grade 9/ Form 3'), ('Grade 10', 'Grade 10/ Form 4'), ('Grade 11', 'Grade 11/ Form 5'), ('Grade 12', 'Grade 12/ Form 6')], max_length=500, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_intern_activities', to='application_intern.applicationintern')),
            ],
        ),
    ]
