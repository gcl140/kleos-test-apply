from django import forms
from .models import ApplicationCohort, Sibling, Dependent, Activity, Distinction

class IntroForm(forms.ModelForm):
    class Meta:
        model =  ApplicationCohort
        fields = [
             'agreed', 
        ]
        
class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = ['first_name', 
            'middle_name', 'last_name',
             'dob', 
             'gender', 
            'nationality',
            'place_of_birth'
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = [
            'residency', 
            'tel1', 'tel2', 'email1', 'email2'
        ]

class SchoolInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = [
            'adv_school_name', 
            'adv_school_phone', 'adv_school_email', 
            'adv_curriculum','report_other_adv', 'other_adv_school_name', 
            'other_adv_school_phone', 'other_adv_school_email', 
            'other_adv_curriculum', 'olv_school_name', 
            'olv_school_phone', 'olv_school_email', 
            'olv_curriculum','report_other_olv', 'other_olv_school_name', 
            'other_olv_school_phone', 'other_olv_school_email', 
            'other_olv_curriculum'
        ]

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = [
            'par1_fname', 
            'par1_mname', 'par1_lname', 'par1_email', 
            'par1_phone', 'par1_retire', 'par1_jobtitle', 'par1_employmentstatus', 'par1_served', 'par1_jobbusy', 
            'par1_levedu', 'par1_institute', 'par1_degree', 'par1_degreeyear',
            
            'report_other_par', 'par2_fname', 
            'par2_mname', 'par2_lname', 'par2_email', 
            'par2_phone', 'par2_retire','par2_jobtitle', 'par2_employmentstatus', 'par2_served', 
            'par2_jobbusy', 'par2_levedu', 'par2_institute', 'par2_degree', 'par2_degreeyear'
        ]

class FinancialInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = [
            # 'siblings', 
            # 'dependents', 
            # 'unbpay', 'unbpayc',
            'f_payer_olevel', 'f_payer_alevel', 
            'o_fee', 'a_fee', 
              'suprt', 'home_fees',
            'suprt_amnt', 'suprt_name', 'suprtc',]

class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = ApplicationCohort
        fields = [
            'fav_hobby',
            'form4_holiday',
            'soc_challenge',
            'has_passport', 
            'passport_purpose', 
            'owns_phone', 
            'phone_maker', 
            'phone_model',
            'sat_for_sat',
            'sat_type',
            'sat_score',
            'sat_date',
            'sat_for_eng',
            'eng_type',
            'eng_score',
            'eng_date', 
            # 'social_media',  
            'known_tansaf_ig', 
            'known_tansaf_fb', 
            'known_tansaf_int', 
            'known_tansaf_tans', 
            'known_tansaf_fam', 
            'known_tansaf_other',
            'known_tansaf_other_write',
        ]
        widgets = {
            'signdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class WritingForm(forms.ModelForm):
    class Meta:
        model =  ApplicationCohort
        fields = [
            'extrac', 'chlg',
            'teach', 'why_you', 
            'why_tansaf', 'covid_impact', 
            'covid_impact_details', 'has_disciplinary_violation', 
            'disciplinary_details', 'additional_circumstances', 'additional_circumstances_details',]

class FinalsForm(forms.ModelForm):
    class Meta:
        model =  ApplicationCohort
        fields = [
            'financial',
            'rec_letter1',
            'rec_letter2',
            # 'ib_scores',
            'adv_certificates',
            'olv_certificates',
            'a_level_school_transcripts', 
            'o_level_school_transcripts', 
            'official_id',
            'supps', 
            'signature', 
            'signdate'
        ]
        widgets = {
            'signdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class SiblingForm(forms.ModelForm):
    class Meta:
        model = Sibling
        fields = ['sibling_name', 'age', 'education', 'institute', 'degree', 'occupation']

class DependentForm(forms.ModelForm):
    class Meta:
        model = Dependent
        fields = ['dependent_name', 'relationship']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'activity_description', 'outside_school', 'leadership_position', 'organization_name', 'start_year', 'end_year', 'weeksperyear', 'hoursperweek']
        
class DistinctionForm(forms.ModelForm):
    class Meta:
        model = Distinction
        fields = ['distinction_name', 'level_of_rec', 'year']






# class ApplicationCohortForm(forms.ModelForm):
#     class Meta:
#         model = ApplicationCohort
#         fields = '__all__'
#         widgets = {
#             'dob': forms.DateInput(attrs={'type': 'date'}),
#             'signdate': forms.DateInput(attrs={'type': 'date'}),
#             'created': forms.DateInput(attrs={'type': 'datetime-local'}),
#             'updated': forms.DateInput(attrs={'type': 'datetime-local'}),
#         }

