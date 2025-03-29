from django.urls import path
from . import views

# from django.conf.urls import handler404
# from applications.views import custom_404_view 
# handler404 = custom_404_view  # Set your custom handler
# handler404 = 'applications.views.custom_404_view'


urlpatterns = [
    path('intro/', views.intro_view, name='intern_intro_view'),
    path('general-info/', views.general_info_view, name='intern_general_info_view'),
    path('contact-info/', views.contact_info_view, name='intern_contact_info_view'),
    path('school-info/', views.school_info_view, name='intern_school_info_view'),
    path('parent-info/', views.parent_info_view, name='intern_parent_info_view'),
    path('financial-info/', views.financial_info_view, name='intern_financial_info_view'),
    path('additional-info/', views.additional_info_view, name='intern_additional_info_view'),
    path('essay-writing/', views.writing_section_view, name='intern_writing_section_view'),
    path('finale/', views.files_signature, name='intern_files_signature'),
    
    path('intern_addactivities/', views.addactivities, name='intern_addactivities'),
    path('intern_create_activity/', views.intern_create_activity, name='intern_create_activity'),
    path('update_activity/<int:activity_id>/', views.update_activity, name='intern_update_activity'), 
    path('delete_activity/<int:activity_id>/', views.delete_activity, name='intern_delete_activity'),
    path('intern_adddistinctions/', views.adddistinctions, name='intern_adddistinctions'),
    path('create_distinction/', views.create_distinction, name='intern_create_distinction'),
    path('update_distinction/<int:distinction_id>/', views.update_distinction, name='intern_update_distinction'), 
    path('delete_distinction/<int:distinction_id>/', views.delete_distinction, name='intern_delete_distinction'),
    path('intern_addsiblings/', views.addsiblings, name='intern_addsiblings'),
    path('create_sibling/', views.create_sibling, name='intern_create_sibling'),
    path('update_sibling/<int:sibling_id>/', views.update_sibling, name='intern_update_sibling'), 
    path('delete_sibling/<int:sibling_id>/', views.delete_sibling, name='intern_delete_sibling'),


    # path('get-sibling-count/', views.get_sibling_count, name='intern_get_sibling_count'),


    path('intern_adddependents/', views.adddependents, name='intern_adddependents'),
    path('create_dependent/', views.create_dependent, name='intern_create_dependent'),
    path('update_dependent/<int:dependent_id>/', views.update_dependent, name='intern_update_dependent'), 
    path('delete_dependent/<int:dependent_id>/', views.delete_dependent, name='intern_delete_dependent'),
    
    path('preview_application/', views.preview_application_view, name='intern_preview_application_view'),
    path('preview_applicationo/<int:user_id>/', views.preview_application_viewo, name='intern_preview_application_viewo'),
    path('view_all_applications/', views.view_all_applications, name='intern_view_all_applications'),

     path('application_submitted/', views.application_submitted_view, name='intern_application_submitted_view'),
   
    # path('success/<int:application_id>/', views.application_success, name='intern_application_success'),
]
