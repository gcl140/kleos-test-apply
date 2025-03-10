from django.contrib import admin
from .models import ApplicationCohort, Sibling, Dependent, Activity, Distinction

class SiblingInline(admin.TabularInline):  # or admin.StackedInline for different layout
    model = Sibling
    extra = 1  # Number of empty forms to display

class DependentInline(admin.TabularInline):  # or admin.StackedInline for different layout
    model = Dependent
    extra = 1  # Number of empty forms to display

class ActivityInline(admin.TabularInline):  # or admin.StackedInline for different layout
    model = Activity
    extra = 1  # Number of empty forms to display

class DistinctionInline(admin.TabularInline):  # or admin.StackedInline for different layout
    model = Distinction
    extra = 1  # Number of empty forms to display

class ApplicationCohortAdmin(admin.ModelAdmin):
        # Fields to display in the list view
    list_display = ('get_username', 'submitted', 'agreed', 'first_name', 'last_name', 'adv_school_name')

    def get_username(self, obj):
        return obj.user.username if obj.user else 'N/A'
    get_username.short_description = 'Username'

    fieldsets = (
        ('Completion', {
            'fields': ('intro_completed', 'general_info_completed', 'contact_info_completed', 'school_info_completed', 
                       'family_info_completed', 'siblings_completed', 'dependents_completed', 'financial_info_completed', 
                       'activities_completed', 'distinctions_completed', 'other_inquiries_completed', 'writing_completed', 
                       'files_signature')
        }),
        ('General Information', {
            'fields': ('submitted', 'user', 'agreed', 'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'nationality', 'place_of_birth')
        }),
        ('Contact Information', {
            'fields': ('residency', 'tel1', 'tel2', 'email1', 'email2')
        }),
        ('School Information', {
            'fields': ('adv_school_name', 'adv_school_phone', 'adv_school_email', 'adv_curriculum', 'report_other_adv', 
                       'other_adv_school_name', 'other_adv_school_phone', 'other_adv_school_email', 'other_adv_curriculum',
                       'olv_school_name', 'olv_school_phone', 'olv_school_email', 'olv_curriculum', 'report_other_olv',
                       'other_olv_school_name', 'other_olv_school_phone', 'other_olv_school_email', 'other_olv_curriculum')
        }),
        ('Parent Information', {
            'fields': ('par1_fname', 'par1_mname', 'par1_lname', 'par1_email', 'par1_phone', 'par1_jobbusy', 'par1_jobtitle',
                       'par1_employmentstatus', 'par1_retire', 'par1_served', 'par1_levedu', 'par1_institute', 'par1_degree',
                       'par1_degreeyear', 'report_other_par', 'par2_fname', 'par2_mname', 'par2_lname', 'par2_email',
                       'par2_phone', 'par2_retire', 'par2_served', 'par2_jobbusy', 'par2_jobtitle', 'par2_employmentstatus',
                       'par2_levedu', 'par2_institute', 'par2_degree', 'par2_degreeyear')
        }),
        ('Financial Information', {
            'fields': ('f_payer_olevel', 'f_payer_alevel', 'o_fee', 'a_fee', 'suprt', 'suprt_amnt', 'suprt_name',
                       'home_fees', 'suprtc')
        }),
        ('Additional Information', {
            'fields': ('fav_hobby', 'form4_holiday', 'soc_challenge', 'sat_for_sat', 'sat_type', 'sat_score', 'sat_date',
                       'sat_for_eng', 'eng_type', 'eng_score', 'eng_date', 'has_passport', 'passport_purpose', 'owns_phone',
                       'phone_maker', 'phone_model', 'known_tansaf_ig', 'known_tansaf_fb', 'known_tansaf_int', 'known_tansaf_tans',
                       'known_tansaf_fam', 'known_tansaf_other', 'known_tansaf_other_write')
        }),
        ('Writing Section', {
            'fields': ('extrac', 'chlg', 'teach', 'why_you', 'why_tansaf', 'covid_impact', 'covid_impact_details',
                       'has_disciplinary_violation', 'disciplinary_details', 'additional_circumstances', 'additional_circumstances_details')
        }),
        ('Files and Signature', {
            'fields': ('financial', 'rec_letter1', 'rec_letter2', 'adv_certificates', 'olv_certificates', 'a_level_school_transcripts',
                       'o_level_school_transcripts', 'official_id', 'supps', 'signature', 'signdate')
        }),
    )

    inlines = [SiblingInline, DependentInline, ActivityInline, DistinctionInline]
    
# Register the model with the custom admin
admin.site.register(ApplicationCohort, ApplicationCohortAdmin)
# admin.site.register(Sibling)  # Register Sibling model
# admin.site.register(Dependent)  # Register Dependent model
# admin.site.register(Activity)  # Register Activity model
# admin.site.register(Distinction)  # Register Distinction model