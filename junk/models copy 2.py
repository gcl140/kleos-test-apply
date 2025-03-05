from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

def user_upload_path(instance, filename):
    # Use the username from the related CustomUser instance to create a folder
    return f"{instance.user.username}/{filename}"

class Application(models.Model):
    # General Information
    user = models.ForeignKey('yuzzaz.CustomUser', on_delete=models.CASCADE)
    agreed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(default=date(2000, 1, 1))
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    nationality = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)

    # Contact Information
    residency = models.CharField(max_length=255)
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, blank=True, null=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True, null=True)

    # School Information
    adv_school_name = models.CharField(max_length=255)
    adv_school_phone = models.CharField(max_length=15)
    adv_school_email = models.EmailField()
    adv_curriculum = models.CharField(max_length=100)
    report_other_adv = models.BooleanField(default=False)
    other_adv_school_name = models.CharField(max_length=255, blank=True, null=True)
    other_adv_school_phone = models.CharField(max_length=15, blank=True, null=True)
    other_adv_school_email = models.EmailField(blank=True, null=True)
    other_adv_curriculum = models.CharField(max_length=100, blank=True, null=True)
    olv_school_name = models.CharField(max_length=255)
    olv_school_phone = models.CharField(max_length=15)
    olv_school_email = models.EmailField()
    olv_curriculum = models.CharField(max_length=100)
    report_other_olv = models.BooleanField(default=False)
    other_olv_school_name = models.CharField(max_length=255, blank=True, null=True)
    other_olv_school_phone = models.CharField(max_length=15, blank=True, null=True)
    other_olv_school_email = models.EmailField(blank=True, null=True)
    other_olv_curriculum = models.CharField(max_length=100, blank=True, null=True)

    # Parent Information
    par1_fname = models.CharField(max_length=100)
    par1_mname = models.CharField(max_length=100, blank=True, null=True)
    par1_lname = models.CharField(max_length=100)
    par1_email = models.EmailField()
    par1_phone = models.CharField(max_length=15)
    par1_jobbusy = models.CharField(max_length=100)
    par1_jobtitle = models.CharField(max_length=100)
    par1_employmentstatus = models.CharField(max_length=100)
    par1_retire = models.DateField(default=date(2000, 1, 1), blank=True, null=True)
    par1_served = models.PositiveIntegerField(default=0)
    par1_levedu = models.CharField(max_length=255, choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('HighSchool', 'High School or Vocational training education'), ('BachelorDeg', 'Bachelors degree or equivalent level'), ('MastersDeg', 'Masters degree or equivalent level'), ('PhD', 'PhD')], default='PhD')
    par1_institute = models.CharField(max_length=255, blank=True, null=True)
    par1_degree = models.CharField(max_length=255, blank=True, null=True)
    par1_degreeyear = models.PositiveIntegerField(default=2000)

    report_other_par = models.BooleanField(default=False)

    par2_fname = models.CharField(max_length=100)
    par2_mname = models.CharField(max_length=100, blank=True, null=True)
    par2_lname = models.CharField(max_length=100)
    par2_email = models.EmailField()
    par2_phone = models.CharField(max_length=15)
    par2_retire = models.DateField(default=date(2000, 1, 1), blank=True, null=True)
    par2_served = models.PositiveIntegerField(default=0)
    par2_jobbusy = models.CharField(max_length=100)
    par2_jobtitle = models.CharField(max_length=100)
    par2_employmentstatus = models.CharField(max_length=100)
    par2_levedu = models.CharField(max_length=255, choices=[('Primary', 'Primary education'), ('Secondary', 'Secondary Education'), ('HighSchool', 'High School or Vocational training education'), ('BachelorDeg', 'Bachelors degree or equivalent level'), ('MastersDeg', 'Masters degree or equivalent level'), ('PhD', 'PhD')], default='PhD')
    par2_institute = models.CharField(max_length=255, blank=True, null=True)
    par2_degree = models.CharField(max_length=255, blank=True, null=True)
    par2_degreeyear = models.PositiveIntegerField(default=2000)

    # Financial Information
    # siblings = models.IntegerField(default=0)
    # dependents = models.IntegerField(default=0)
    f_payer_olevel = models.CharField(max_length=255)
    f_payer_alevel = models.CharField(max_length=255)
    o_fee = models.FloatField(default=0.0)
    a_fee = models.FloatField(default=0.0)
    unbpay = models.TextField(blank=True, null=True)
    unbpayc = models.CharField(max_length=255, blank=True, null=True)
    suprt = models.BooleanField(default=False)
    suprt_amnt = models.FloatField(blank=True, null=True)
    suprt_name = models.CharField(max_length=255, blank=True, null=True)
    home_fees = models.BooleanField(default=False)
    suprtc = models.TextField( blank=True, null=True)

    # Additional Information
    form_4_holiday = models.TextField(blank=True, null=True)
    fav_hobby = models.TextField(blank=True, null=True)
    sat_for_sat = models.BooleanField(default=False)
    sat_type = models.CharField(max_length=255, blank=True, null=True)
    sat_score = models.CharField(max_length=255, blank=True, null=True)
    sat_date = models.DateField(default=date(2000, 1, 1), blank=True, null=True)
    sat_for_eng = models.BooleanField(default=False)
    eng_type = models.CharField(max_length=255, blank=True, null=True)
    eng_score = models.CharField(max_length=255, blank=True, null=True)
    eng_score = models.CharField(max_length=255, blank=True, null=True)
    eng_date = models.DateField(default=date(2000, 1, 1), blank=True, null=True)
    has_passport = models.BooleanField(default=False)
    passport_purpose = models.TextField(blank=True, null=True)
    owns_phone = models.BooleanField(default=False)
    phone_maker = models.CharField(max_length=255, blank=True, null=True)
    phone_model = models.CharField(max_length=255, blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    distinctions = models.TextField(blank=True, null=True)
    extrac = models.TextField(blank=True, null=True)
    chlg = models.TextField(blank=True, null=True)
    cohort = models.TextField(blank=True, null=True)
    social_media = models.TextField(blank=True, null=True)
    teach = models.TextField(blank=True, null=True)
    why_you = models.TextField(blank=True, null=True)
    why_tansaf = models.TextField(blank=True, null=True)
    covid_impact = models.BooleanField(default=False)
    covid_impact_details = models.TextField(blank=True, null=True)
    has_disciplinary_violation = models.BooleanField(default=False)
    disciplinary_details = models.TextField(blank=True, null=True)
    additional_circumstances = models.BooleanField(default=False)
    additional_circumstances_details = models.TextField(blank=True, null=True)

    known_tansaf_ig = models.BooleanField(default=False) 
    known_tansaf_fb = models.BooleanField(default=False)
    known_tansaf_int = models.BooleanField(default=False)
    known_tansaf_tans = models.BooleanField(default=False)
    known_tansaf_fam = models.BooleanField(default=False)
    known_tansaf_other = models.BooleanField(default=False)
    known_tansaf_other_write = models.CharField(max_length=255, blank=True, null=True)

    csee_results = models.FileField(upload_to=user_upload_path, blank=True, null=True)
    school_transcripts = models.FileField(upload_to="profile_pics/", blank=True, null=True)
    official_id = models.FileField(upload_to="profile_pics/", blank=True, null=True)
    supps = models.FileField(upload_to="profile_pics/", blank=True, null=True)
    signature  = models.CharField(max_length=255)
    signed = models.BooleanField(default=False)
    signdate = models.DateField(default=date(2000, 1, 1), blank=True, null=True)  # Default to 1st January 2000
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sibling(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_siblings")
    sibling_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=255)
    institute = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.sibling_name} - {self.age}"

class Dependent(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_dependents")
    dependent_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dependent_name} - {self.relationship}"

class Activity(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_activities")
    activity_type = models.CharField(max_length=255)
    leadership_position = models.CharField(max_length=255, null=True, blank=True)
    organization_name = models.CharField(max_length=2555, null=True, blank=True)
    activity_description = models.TextField(blank=True, null=True)
    outside_school = models.BooleanField(default=False)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.activity_type} at {self.organization_name}"

class Distinction(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_distinctions")
    distinction_name = models.CharField(max_length=255)
    level_of_rec = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

    def __str__(self):        
        return f"{self.distinction_name} - {self.level_of_rec}"
