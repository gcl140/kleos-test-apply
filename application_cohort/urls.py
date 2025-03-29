from django.urls import path
from . import views

# from django.conf.urls import handler404
# from applications.views import custom_404_view 
# handler404 = custom_404_view  # Set your custom handler
# handler404 = 'applications.views.custom_404_view'


urlpatterns = [
    path('intro/', views.intro_view, name='intro_view'),
    path('general-info/', views.general_info_view, name='general_info_view'),
    path('contact-info/', views.contact_info_view, name='contact_info_view'),
    path('school-info/', views.school_info_view, name='school_info_view'),
    path('parent-info/', views.parent_info_view, name='parent_info_view'),
    path('financial-info/', views.financial_info_view, name='financial_info_view'),
    path('additional-info/', views.additional_info_view, name='additional_info_view'),
    path('essay-writing/', views.writing_section_view, name='writing_section_view'),
    path('finale/', views.files_signature, name='files_signature'),
    
    path('addactivities/', views.addactivities, name='addactivities'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('update_activity/<int:activity_id>/', views.update_activity, name='update_activity'), 
    path('delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('adddistinctions/', views.adddistinctions, name='adddistinctions'),
    path('create_distinction/', views.create_distinction, name='create_distinction'),
    path('update_distinction/<int:distinction_id>/', views.update_distinction, name='update_distinction'), 
    path('delete_distinction/<int:distinction_id>/', views.delete_distinction, name='delete_distinction'),
    path('addsiblings/', views.addsiblings, name='addsiblings'),
    path('create_sibling/', views.create_sibling, name='create_sibling'),
    path('update_sibling/<int:sibling_id>/', views.update_sibling, name='update_sibling'), 
    path('delete_sibling/<int:sibling_id>/', views.delete_sibling, name='delete_sibling'),


    # path('get-sibling-count/', views.get_sibling_count, name='get_sibling_count'),


    path('adddependents/', views.adddependents, name='adddependents'),
    path('create_dependent/', views.create_dependent, name='create_dependent'),
    path('update_dependent/<int:dependent_id>/', views.update_dependent, name='update_dependent'), 
    path('delete_dependent/<int:dependent_id>/', views.delete_dependent, name='delete_dependent'),
    
    path('preview_application/', views.preview_application_view, name='preview_application_view'),
    # path('preview_applicationo/<int:user_id>/', views.preview_application_viewo, name='preview_application_viewo'),
    # path('view_all_applications/', views.view_all_applications, name='view_all_applications'),

     path('application_submitted/', views.application_submitted_view, name='application_submitted_view'),
   
    # path('success/<int:application_id>/', views.application_success, name='application_success'),
]
