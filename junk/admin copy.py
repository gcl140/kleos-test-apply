from django.contrib import admin
from .models import Application
from yuzzaz.models import CustomUser
import json

class ApplicationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'get_username','agreed', 'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'nationality', 'residency',
        'tel1', 'email1', 'adv_school_name', 'olv_school_name', 'par1_fname', 'par1_lname',
        'siblings', 'dependents', 'signed', 'created', 'updated', 'stage_1_data_display', 'stage_2_data_display'
    )
    def get_username(self, obj):
        return obj.user.username if obj.user else 'N/A'
    get_username.short_description = 'Username'
    # Search fields for quick lookup in the admin panel
    search_fields = ('first_name', 'last_name', 'email1', 'dob')
    
    # Fields that will have filtering options in the sidebar
    list_filter = ('gender', 'signed', 'nationality', 'created')
    
    # Fields that can be edited in the list view
    list_editable = ('signed',)
    
    # Ordering in the list view
    ordering = ('-created',)
    
    # Fieldsets to organize form layout in admin edit view
    fieldsets = (
        ('General Information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'dob', 'gender', 'nationality')
        }),
        ('Contact Information', {
            'fields': ('residency', 'tel1', 'tel2', 'email1', 'email2')
        }),
        ('School Information', {
            'fields': ('adv_school_name', 'adv_school_phone', 'adv_school_email', 'adv_curriculum',
                       'olv_school_name', 'olv_school_phone', 'olv_school_email', 'olv_curriculum')
        }),
        ('Parent Information', {
            'fields': ('par1_fname', 'par1_mname', 'par1_lname', 'par1_email', 'par1_phone', 'par1_retire')
        }),
        ('Financial Information', {
            'fields': ('siblings', 'dependents', 'f_payer_olevel', 'f_payer_alevel', 'o_fee', 'a_fee')
        }),
        ('Additional Information', {
            'fields': ('activities', 'distinctions', 'extrac', 'chlg', 'social_media', 'teach', 'why_you')
        }),
        ('Metadata', {
            'fields': ('signed', 'signdate')  # Removed 'created' and 'updated' as they are non-editable
        }),
        ('Form Data', {
            'fields': ('stage_1_data', 'stage_2_data')  # Add JSON fields here if needed
        })
    )

    # Custom methods to display JSON field data more readably in the list view
    def stage_1_data_display(self, obj):
        # You can extract specific data from the JSON field if you prefer
        # For example, show the first name from the stage_1_data JSON
        return obj.stage_1_data.get('first_name', 'N/A') if obj.stage_1_data else 'N/A'

    def stage_2_data_display(self, obj):
        # Similarly for stage_2_data
        return obj.stage_2_data.get('last_name', 'N/A') if obj.stage_2_data else 'N/A'

# Register the model with the custom admin
admin.site.register(Application, ApplicationAdmin)
