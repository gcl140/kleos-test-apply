from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



# def user_upload_path(instance, filename):
#     return f"{instance.user.username}/{filename}"

def user_upload_path(instance, filename):
    # Replace '@' with an underscore or any other character
    username = instance.user.username.replace('@', '_')
    return f"cohort/{username}/{filename}"


class ApplicationCohort(models.Model):
    NATIONALITIES = [
        ('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'),
        ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'),
        ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'),
        ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BR', 'Brazil'),
        ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'), ('CM', 'Cameroon'),
        ('CA', 'Canada'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'),
        ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo (DRC)'),
        ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'),
        ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'),
        ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'),
        ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GR', 'Greece'),
        ('GD', 'Grenada'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'),
        ('GY', 'Guyana'), ('HT', 'Haiti'), ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'),
        ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'),
        ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'Korea (North)'), ('KR', 'Korea (South)'),
        ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'),
        ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'),
        ('MO', 'Macau'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'),
        ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'),
        ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'),
        ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'),
        ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'),
        ('NE', 'Niger'), ('NG', 'Nigeria'), ('MK', 'North Macedonia'), ('NO', 'Norway'), ('OM', 'Oman'),
        ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'),
        ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'),
        ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'),
        ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'),
        ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'),
        ('SO', 'Somalia'), ('ZA', 'South Africa'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'),
        ('SD', 'Sudan'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'),
        ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'),
        ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'),
        ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'),
        ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')
    ]
    # General Information
    submitted = models.BooleanField(default=False)
    user = models.ForeignKey('yuzzaz.CustomUser', on_delete=models.CASCADE)
    agreed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=500)
    middle_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500)
    dob = models.DateField(default=date(2025, 1, 1))
    gender = models.CharField(max_length=50, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    nationality = models.CharField(max_length=500, choices=NATIONALITIES, default='TZ')
    place_of_birth = models.CharField(max_length=500)

    # Contact Information
    residency = models.TextField(max_length=500)
    tel1 = PhoneNumberField()
    tel2 = PhoneNumberField(blank=True, null=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True, null=True)

    # School Information
    adv_school_name = models.CharField(max_length=500)
    adv_school_phone = PhoneNumberField()
    adv_school_email = models.EmailField()
    adv_curriculum = models.CharField(max_length=500, choices=[ ('NECTA', 'NECTA'), ('IB', 'IB'), ('CAMBRIDGE', 'Cambridge'), ('OTHER', 'Other'), ], default='NECTA')
    report_other_adv = models.BooleanField(default=False)
    other_adv_school_name = models.CharField(max_length=500, blank=True, null=True)
    other_adv_school_phone = PhoneNumberField(blank=True, null=True)
    other_adv_school_email = models.EmailField(blank=True, null=True)
    other_adv_curriculum = models.CharField(max_length=500, choices=[ ('NECTA', 'NECTA'), ('IB', 'IB'), ('CAMBRIDGE', 'Cambridge'), ('OTHER', 'Other'), ], blank=True, null=True)
    olv_school_name = models.CharField(max_length=500)
    olv_school_phone = PhoneNumberField()
    olv_school_email = models.EmailField()
    olv_curriculum = models.CharField(max_length=500, choices=[ ('NECTA', 'NECTA'), ('IB', 'IB'), ('CAMBRIDGE', 'Cambridge'), ('OTHER', 'Other'), ], default='NECTA' )
    report_other_olv = models.BooleanField(default=False)
    other_olv_school_name = models.CharField(max_length=500, blank=True, null=True)
    other_olv_school_phone = PhoneNumberField(blank=True, null=True)
    other_olv_school_email = models.EmailField(blank=True, null=True)
    other_olv_curriculum = models.CharField(max_length=500, choices=[ ('NECTA', 'NECTA'), ('IB', 'IB'), ('CAMBRIDGE', 'Cambridge'), ('OTHER', 'Other'), ] , blank=True, null=True)

    # Parent Information
    par1_fname = models.CharField(max_length=500)
    par1_mname = models.CharField(max_length=500, blank=True, null=True)
    par1_lname = models.CharField(max_length=500)
    par1_email = models.EmailField()
    par1_phone = PhoneNumberField()
    par1_jobbusy = models.CharField(max_length=500)
    par1_jobtitle = models.CharField(max_length=500, blank=True, null=True)
    par1_employmentstatus = models.CharField(max_length=500, choices=[ ('Employed', 'Employed'), ('Self Employed', 'Self Employed'), ('Unemployed', 'Unemployed'), ('Retired', 'Retired'), ])
    par1_retire = models.DateField(blank=True, null=True)
    par1_served = models.PositiveIntegerField(default=0)
    par1_levedu = models.CharField(max_length=500, choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('High School', 'High School or Vocational training education'), ('Bachelor degree', 'Bachelors degree or equivalent level'), ('Masters Degree', 'Masters degree or equivalent level'), ('PhD', 'PhD')], blank=True, null=True)
    par1_institute = models.CharField(max_length=500, blank=True, null=True)
    par1_degree = models.CharField(max_length=500, blank=True, null=True)
    par1_degreeyear = models.PositiveIntegerField(blank=True, null=True)

    report_other_par = models.BooleanField(default=False)

    par2_fname = models.CharField(max_length=500,  blank=True, null=True)
    par2_mname = models.CharField(max_length=500, blank=True, null=True)
    par2_lname = models.CharField(max_length=500,  blank=True, null=True)
    par2_email = models.EmailField( blank=True, null=True)
    par2_phone = PhoneNumberField( blank=True, null=True)
    par2_retire = models.DateField(blank=True, null=True)
    par2_served = models.PositiveIntegerField(default=0,  blank=True, null=True)
    par2_jobbusy = models.CharField(max_length=500,  blank=True, null=True)
    par2_jobtitle = models.CharField(max_length=500,  blank=True, null=True)
    par2_employmentstatus = models.CharField(max_length=500, choices=[ ('Employed', 'Employed'), ('Self Employed', 'Self Employed'), ('Unemployed', 'Unemployed'), ('Retired', 'Retired'), ],  blank=True, null=True)
    par2_levedu = models.CharField(max_length=500, choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('High School', 'High School or Vocational training education'), ('Bachelor degree', 'Bachelors degree or equivalent level'), ('Masters Degree', 'Masters degree or equivalent level'), ('PhD', 'PhD')],blank=True, null=True)
    par2_institute = models.CharField(max_length=500, blank=True, null=True)
    par2_degree = models.CharField(max_length=500, blank=True, null=True)
    par2_degreeyear = models.PositiveIntegerField(blank=True, null=True)

    # Financial Information
    f_payer_olevel = models.CharField(max_length=500)
    f_payer_alevel = models.CharField(max_length=500)
    o_fee = models.FloatField(default=0.0)
    a_fee = models.FloatField(default=0.0)
    suprt = models.BooleanField(default=False)
    suprt_amnt = models.FloatField(blank=True, null=True)
    suprt_name = models.CharField(max_length=500, blank=True, null=True)
    home_fees = models.BooleanField(default=False)
    suprtc = models.TextField( blank=True, null=True)


    # Additional Information
    fav_hobby = models.TextField(blank=True, null=True)
    form4_holiday = models.TextField(blank=True, null=True)
    soc_challenge = models.TextField(blank=True, null=True)
    sat_for_sat = models.BooleanField(default=False)
    sat_type = models.CharField(max_length=500, blank=True, null=True, choices=[('SAT','SAT'), ('SAT Subject Test','SAT Subject Test'), ('ACT','ACT'), ('AP','AP'), ('Other','Other')])
    sat_score = models.CharField(max_length=500, blank=True, null=True)
    sat_date = models.DateField(blank=True, null=True)
    sat_for_eng = models.BooleanField(default=False)
    eng_type = models.CharField(max_length=500, blank=True, null=True, choices=[('TOEFL','TOEFL'), ('IELTS','IELTS'), ('Duolingo','Duolingo'), ('Other','Other')])
    eng_score = models.CharField(max_length=500, blank=True, null=True)
    eng_date = models.DateField(blank=True, null=True)
    has_passport = models.BooleanField(default=False)
    passport_purpose = models.TextField(blank=True, null=True)
    owns_phone = models.BooleanField(default=False)
    phone_maker = models.CharField(max_length=500, blank=True, null=True)
    phone_model = models.CharField(max_length=500, blank=True, null=True)
    known_tansaf_ig = models.BooleanField(default=False) 
    known_tansaf_fb = models.BooleanField(default=False)
    known_tansaf_int = models.BooleanField(default=False)
    known_tansaf_tans = models.BooleanField(default=False)
    known_tansaf_fam = models.BooleanField(default=False)
    known_tansaf_other = models.BooleanField(default=False)
    known_tansaf_other_write = models.CharField(max_length=500, blank=True, null=True)

    # Writing Section
    extrac = models.TextField()
    chlg = models.TextField()
    teach = models.TextField()
    why_you = models.TextField()
    why_tansaf = models.TextField()
    covid_impact = models.BooleanField(default=False)
    covid_impact_details = models.TextField(blank=True, null=True)
    has_disciplinary_violation = models.BooleanField(default=False)
    disciplinary_details = models.TextField(blank=True, null=True)
    additional_circumstances = models.BooleanField(default=False)
    additional_circumstances_details = models.TextField(blank=True, null=True)

    #Files and Signature
    financial = models.FileField(upload_to=user_upload_path)
    rec_letter1 = models.FileField(upload_to=user_upload_path)
    rec_letter2 = models.FileField(upload_to=user_upload_path, blank=True, null=True)
    adv_certificates = models.FileField(upload_to=user_upload_path, blank=True, null=True)
    olv_certificates = models.FileField(upload_to=user_upload_path)
    a_level_school_transcripts = models.FileField(upload_to=user_upload_path)
    o_level_school_transcripts = models.FileField(upload_to=user_upload_path)
    official_id = models.FileField(upload_to=user_upload_path)
    supps = models.FileField(upload_to=user_upload_path, blank=True, null=True)
    signature  = models.CharField(max_length=500)
    signdate = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    # Form Completion Tracking
    intro_completed = models.BooleanField(default=False)
    general_info_completed = models.BooleanField(default=False)
    contact_info_completed = models.BooleanField(default=False)
    school_info_completed = models.BooleanField(default=False)
    family_info_completed = models.BooleanField(default=False)
    siblings_completed = models.BooleanField(default=True)
    dependents_completed = models.BooleanField(default=True)
    financial_info_completed = models.BooleanField(default=False)
    activities_completed = models.BooleanField(default=True)
    distinctions_completed = models.BooleanField(default=True)
    other_inquiries_completed = models.BooleanField(default=True)
    writing_completed = models.BooleanField(default=False)
    # essay = models.BooleanField(default=False)
    files_signature = models.BooleanField(default=False) 
    
    def get_completion_status(self):
        """Returns a dictionary with the completion status of each form section"""
        return {
            'intro': {
                'completed': self.intro_completed,
                'url': 'intro_view'
            },
            'general_info': {
                'completed': self.general_info_completed,
                'url': 'general_info_view'
            },
            'contact_info': {
                'completed': self.contact_info_completed,
                'url': 'contact_info_view'
            },
            'school_info': {
                'completed': self.school_info_completed,
                'url': 'school_info_view'
            },
            'family_info': {
                'completed': self.family_info_completed,
                'url': 'parent_info_view'
            },
            'siblings': {
                'completed': self.siblings_completed,
                'url': 'addsiblings'
            },
            'dependents': {
                'completed': self.dependents_completed,
                'url': 'adddependents'
            },
            'financial_info': {
                'completed': self.financial_info_completed,
                'url': 'financial_info_view'
            },
            'activities': {
                'completed': self.activities_completed,
                'url': 'addactivities'
            },
            'distinctions': {
                'completed': self.distinctions_completed,
                'url': 'adddistinctions'
            },
            'other_inquiries': {
                'completed': self.other_inquiries_completed,
                'url': 'additional_info_view'                
            },
            'writing': {
                'completed': self.writing_completed,
                # 'url': 'essays_view'
                'url': 'writing_section_view'

            },
            'files_signature': {
                'completed': self.files_signature,
                'url': 'files_signature'
            }
        }

    def update_completion_status(self):
        """Updates completion status for all sections based on field completion."""
        self.siblings_completed = True
        self.dependents_completed = True
        self.activities_completed = True
        self.distinctions_completed = True
        self.intro_completed = self.agreed
        self.general_info_completed = all([
            self.first_name, 
            self.last_name, 
            self.dob != date(2025, 1, 1),
            self.gender, 
            self.nationality, 
            self.place_of_birth
        ])
        self.contact_info_completed = all([
            self.residency, 
            self.tel1, 
            self.email1
        ])
        self.school_info_completed = all([
            self.adv_school_name,
            self.adv_school_phone,
            self.adv_school_email,
            self.adv_curriculum,
            self.olv_school_name,
            self.olv_school_phone,
            self.olv_school_email,
            self.olv_curriculum
        ])
        self.family_info_completed = all([
            self.par1_fname,
            self.par1_lname,
            self.par1_phone,
            self.par1_email
        ])
        self.financial_info_completed = all([
            self.f_payer_olevel,
            self.f_payer_alevel,
            self.o_fee >= 0,
            self.a_fee >= 0
        ])
        self.other_inquiries_completed = True
        self.writing_completed = all([
            self.extrac,
            self.chlg,
            self.teach,
            self.why_you,
            self.why_tansaf,
        ])
        self.files_signature = all([
            self.financial and self.financial.name != '',  # Check if file is uploaded
            self.rec_letter1 and self.rec_letter1.name != '',
            self.olv_certificates and self.olv_certificates.name != '',
            self.a_level_school_transcripts and self.a_level_school_transcripts.name != '',
            self.official_id and self.official_id.name != '',
            self.signature and self.signature.strip() != ''
        ])

        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sibling(models.Model):
    application = models.ForeignKey(ApplicationCohort, on_delete=models.CASCADE, related_name="application_cohort_siblings")
    sibling_name = models.CharField(max_length=500, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    education = models.CharField(max_length=500, choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('High School', 'High School or Vocational training education'), ('Bachelor degree', 'Bachelors degree or equivalent level'), ('Masters', 'Masters degree or equivalent level'), ('PhD', 'PhD')], blank=True, null=True)
    institute = models.CharField(max_length=500, null=True, blank=True)
    degree = models.CharField(max_length=500, null=True, blank=True)
    occupation = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.sibling_name} - {self.age}"

class Dependent(models.Model):
    application = models.ForeignKey(ApplicationCohort, on_delete=models.CASCADE, related_name="application_cohort_dependents")
    dependent_name = models.CharField(max_length=500, null=True, blank=True)
    relationship = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.dependent_name} - {self.relationship}"

class Activity(models.Model):
    application = models.ForeignKey(ApplicationCohort, on_delete=models.CASCADE, related_name="application_cohort_activities")
    activity_type = models.CharField(max_length=500, choices=[ ('Academic', 'Academic'),
                                ('Art', 'Art'),
                                ('Athletics', 'Athletics'),
                                ('Community Service', 'Community Service'),
                                ('Computer/Technology', 'Computer/Technology'),
                                ('Cultural', 'Cultural'),
                                ('Dance', 'Dance'),
                                ('Debate/Speech', 'Debate/Speech'),
                                ('Environmental', 'Environmental'),
                                ('Family Responsibilities', 'Family Responsibilities'),
                                ('Foreign Exchange', 'Foreign Exchange'),
                                ('Foreign Language', 'Foreign Language'),
                                ('Journalism', 'Journalism'),
                                ('Music: Instrumental', 'Music: Instrumental'),
                                ('Music: Vocal', 'Music: Vocal'),
                                ('Religious', 'Religious'),
                                ('Research', 'Research'),
                                ('Robotics', 'Robotics'),
                                ('School spirit', 'School spirit'),
                                ('Robotics', 'Robotics'),
                                ('Science/Math', 'Science/Math'),
                                ('Social Justice', 'Social Justice'),
                                ('Student Govt./Politics', 'Student Govt./Politics'),
                                ('Theatre/Drama', 'Theatre/Drama'),
                                ('Work(Paid)', 'Work(Paid)'),
                                ('Other Club/Activity', 'Other Club/Activity'),
])
    leadership_position = models.CharField(max_length=500, null=True, blank=True)
    organization_name = models.CharField(max_length=5005, null=True, blank=True)
    weeksperyear = models.PositiveIntegerField(null=True, blank=True)
    hoursperweek = models.PositiveIntegerField(null=True, blank=True)
    activity_description = models.TextField(blank=True, null=True)
    outside_school = models.BooleanField(default=False)
    start_year = models.CharField(max_length=500, choices=[('Grade 9','Grade 9/ Form 3'),('Grade 10','Grade 10/ Form 4'),('Grade 11','Grade 11/ Form 5'),('Grade 12','Grade 12/ Form 6')], null=True, blank=True)
    end_year = models.CharField(max_length=500, null=True, blank=True, choices=[('Grade 9','Grade 9/ Form 3'),('Grade 10','Grade 10/ Form 4'),('Grade 11','Grade 11/ Form 5'),('Grade 12','Grade 12/ Form 6')])

    def __str__(self):
        return f"{self.activity_type} at {self.organization_name}"

class Distinction(models.Model):
    application = models.ForeignKey(ApplicationCohort, on_delete=models.CASCADE, related_name="application_cohort_distinctions")
    distinction_name = models.CharField(max_length=500, null=True, blank=True)
    level_of_rec = models.CharField(max_length=500, choices=[
                                ('School', 'School'),
                                ('District', 'District'),
                                ('Regional', 'Regional'),
                                ('National', 'National'),
                                ('International', 'International'),], null=True, blank=True)
    year = models.CharField(max_length=500, choices=[('Grade 9','Grade 9/ Form 3'),('Grade 10','Grade 10/ Form 4'),('Grade 11','Grade 11/ Form 5'),('Grade 12','Grade 12/ Form 6')], null=True, blank=True)

    def __str__(self):        
        return f"{self.distinction_name} - {self.level_of_rec}"
