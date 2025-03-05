from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import IntroForm, GeneralInfoForm, ContactInfoForm, SchoolInfoForm, ParentInfoForm, FinancialInfoForm, AdditionalInfoForm, DependentForm, DistinctionForm, SiblingForm, ActivityForm, WritingForm, FinalsForm
from .models import Application, Sibling, Dependent, Distinction, Activity
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.generic import UpdateView

User = get_user_model()
def is_staff_user(user):
    return user.is_staff or user.has_perm('applications.view_all_applications')


def get_application_for_user(user):
    application, created = Application.objects.get_or_create(user=user)
    if created:
        print("A new Application instance was created.")
    else:
        print("Retrieved an existing Application instance.")
    return application

# def save_application_data(application, form):
#     if form.is_valid():
#         for field, value in form.cleaned_data.items():
#             setattr(application, field, value)
#         application.save()
#         return True
#     return False

def save_application_data(application, form, request=None):
    if form.is_valid():
        for field, value in form.cleaned_data.items():
            setattr(application, field, value)
        application.save()
        return True
    else:
        if request:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in '{field}': {error}")
        return False

def get_form_progress_data(application, request):
    """Get progress data for the form progress bar"""
    application = Application.objects.get(user=request.user)
    completion_status = application.get_completion_status()
    
    progress_data = {
        'intro': {
            'label': 'Introduction',
            'url': reverse('intro_view'),
            'completed': completion_status['intro']
        },
        'general_info': {
            'label': 'General Info',
            'url': reverse('general_info_view'),
            'completed': completion_status['general_info']
        },
        'contact_info': {
            'label': 'Contact Info',
            'url': reverse('contact_info_view'),
            'completed': completion_status['contact_info']
        },
        'school_info': {
            'label': 'School Info',
            'url': reverse('school_info_view'),
            'completed': completion_status['school_info']
        },
        'family_info': {
            'label': 'Family Info',
            'url': reverse('parent_info_view'),
            'completed': completion_status['family_info']
        },
        'siblings': {
            'label': 'Siblings',
            'url': reverse('addsiblings'),
            'completed': completion_status['siblings']
        },
        'dependents': {
            'label': 'Dependents',
            'url': reverse('adddependents'),
            'completed': completion_status['dependents']
        },
        'financial_info': {
            'label': 'Financial Info',
            'url': reverse('financial_info_view'),
            'completed': completion_status['financial_info']
        },
        'activities': {
            'label': 'Activities',
            'url': reverse('addactivities'),
            'completed': completion_status['activities']
        },
        'distinctions': {
            'label': 'Distinctions',
            'url': reverse('adddistinctions'),
            'completed': completion_status['distinctions']
        },
        'other_inquiries': {
            'label': 'Other Inquiries',
            'url': reverse('additional_info_view'),
            'completed': completion_status['other_inquiries']
        },
        'writing': {
            'label': 'Writing',
            'url': reverse('writing_section_view'),
            'completed': completion_status['writing']
        },
        'files_signature': {
            'label': 'Files & Signature',
            'url': reverse('files_signature'),
            'completed': completion_status['files_signature']
        }
    }
    
    return progress_data


def get_progress_data(request):
    """Get progress data for the current user's application"""
    if not request.user.is_authenticated:
        return None
    try:
        application = Application.objects.get(user=request.user)
        return application.get_completion_status()
    
    except Application.DoesNotExist:
        return {  # Return default values instead of None
            'intro': False,
            'general_info': False,
            'contact_info': False,
            'school_info': False,
            'family_info': False,
            'siblings': False,
            'dependents': False,
            'financial_info': False,
            'activities': False,
            'distinctions': False,
            'other_inquiries': False,
            'writing': False,
            'files_signature': False
        }

class FormMixin:
    """Mixin to add progress data to context"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress_data'] = get_progress_data(self.request)
        context['current_section'] = self.current_section
        return context

class GeneralInfoView(FormMixin, UpdateView):
    current_section = 'general_info'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

class ContactInfoView(FormMixin, UpdateView):
    current_section = 'contact_info'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

class SchoolInfoView(FormMixin, UpdateView):
    current_section = 'school_info'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

class ParentInfoView(FormMixin, UpdateView):
    current_section = 'family_info'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response
    
class AdditionalInfoView(FormMixin, UpdateView):
    current_section = 'other_inquiries'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

@login_required
def intro_view(request):
    application = get_application_for_user(request.user)

    if request.method == "POST":
        form = IntroForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Intro Form!")
            return redirect('general_info_view')
    else:
        form = IntroForm(instance=application)

    context = {
        'form': form,
        'title': "Introduction",
        'previous_url': None,
        'progress_data': get_form_progress_data(application),
        'current_section': 'intro'
    }
    return render(request, 'applications/1_intro.html', context)

# @login_required
# def general_info_view(request):
#     application = get_application_for_user(request.user)

#     if request.method == 'POST':
#         form = GeneralInfoForm(request.POST, instance=application)
#         if form.is_valid():
#             # application = form.save()
#             form.save()
#             application.update_completion_status()
#             messages.success(request, 'General information updated successfully.')
#             return redirect('contact_info_view')
#     else:
#         form = GeneralInfoForm(instance=application)
    
#     context = {
#         'form': form,
#         'progress_data': get_progress_data(request),
#         'current_section': 'general_info',
#         'previous_url': reverse('intro_view')
#     }
#     return render(request, 'applications/2_general_info.html', context)

@login_required
def general_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == 'POST':
        form = GeneralInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  # Passing the request
            application.update_completion_status()
            messages.success(request, 'General information updated successfully.')
            return redirect('contact_info_view')
    else:
        form = GeneralInfoForm(instance=application)
    
    context = {
        'form': form,
        'progress_data': get_progress_data(request),
        'current_section': 'general_info',
        'previous_url': reverse('intro_view')
    }
    return render(request, 'applications/2_general_info.html', context)

# @login_required
# def contact_info_view(request):
#     application = get_application_for_user(request.user)

#     if request.method == 'POST':
#         form = ContactInfoForm(request.POST, instance=application)
#         if form.is_valid():
#             application = form.save()
#             application.update_completion_status()  
#             messages.success(request, 'Contact information updated successfully.')
#             return redirect('school_info_view')
#     else:
#         form = ContactInfoForm(instance=application)
    
#     context = {
#         'form': form,
#         'progress_data': get_progress_data(request),
#         'current_section': 'contact_info',
#         'previous_url': reverse('general_info_view')
#     }
#     return render(request, 'applications/3_contact_info.html', context)

# @login_required
# def school_info_view(request):
#     application = get_application_for_user(request.user)

#     if request.method == 'POST':
#         form = SchoolInfoForm(request.POST, instance=application)
#         if form.is_valid():
#             application = form.save()
#             application.update_completion_status()  
#             messages.success(request, 'School information updated successfully.')
#             return redirect('parent_info_view')
#     else:
#         form = SchoolInfoForm(instance=application)
    
#     context = {
#         'form': form,
#         'progress_data': get_progress_data(request),
#         'current_section': 'school_info',
#         'previous_url': reverse('contact_info_view')
#     }
#     return render(request, 'applications/4_school_info.html', context)

# @login_required
# def parent_info_view(request):
#     application = get_application_for_user(request.user)

#     if request.method == 'POST':
#         form = ParentInfoForm(request.POST, instance=application)
#         if form.is_valid():
#             application = form.save()
#             application.update_completion_status()  
#             messages.success(request, 'Parent information updated successfully.')
#             return redirect('addsiblings')
#     else:
#         form = ParentInfoForm(instance=application)
    
#     context = {
#         'form': form,
#         'progress_data': get_progress_data(request),
#         'current_section': 'family_info',
#         'previous_url': reverse('school_info_view')
#     }
#     return render(request, 'applications/5_parents_info.html', context)

# @login_required
# def contact_info_view(request):
#     application = get_application_for_user(request.user)

#     if request.method == 'POST':
#         form = ContactInfoForm(request.POST, instance=application)
#         if save_application_data(application, form, request):  # Using save_application_data
#             application.update_completion_status()
#             messages.success(request, 'Contact information updated successfully.')
#             return redirect('school_info_view')
#     else:
#         form = ContactInfoForm(instance=application)
    
#     context = {
#         'form': form,
#         'progress_data': get_progress_data(request),
#         'current_section': 'contact_info',
#         'previous_url': reverse('general_info_view')
#     }
#     return render(request, 'applications/3_contact_info.html', context)

@login_required
def contact_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):
            application.update_completion_status()
            messages.success(request, 'Contact information updated successfully.')
            return redirect('school_info_view')
    else:
        form = ContactInfoForm(instance=application)
    
    # Update context to use `get_form_progress_data`
    context = {
        'form': form,
        'progress_data': get_form_progress_data(application, request),  # Use updated function
        'current_section': 'contact_info',
        'previous_url': reverse('general_info_view')
    }
    return render(request, 'applications/3_contact_info.html', context)

@login_required
def school_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == 'POST':
        form = SchoolInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  # Using save_application_data
            application.update_completion_status()
            messages.success(request, 'School information updated successfully.')
            return redirect('parent_info_view')
    else:
        form = SchoolInfoForm(instance=application)
    
    context = {
        'form': form,
        'progress_data': get_progress_data(request),
        'current_section': 'school_info',
        'previous_url': reverse('contact_info_view')
    }
    return render(request, 'applications/4_school_info.html', context)

@login_required
def parent_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == 'POST':
        form = ParentInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  # Using save_application_data
            application.update_completion_status()
            messages.success(request, 'Parent information updated successfully.')
            return redirect('addsiblings')
    else:
        form = ParentInfoForm(instance=application)
    
    context = {
        'form': form,
        'progress_data': get_progress_data(request),
        'current_section': 'family_info',
        'previous_url': reverse('school_info_view')
    }
    return render(request, 'applications/5_parents_info.html', context)

@login_required
def financial_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == "POST":
        form = FinancialInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Financial Information!")
            return redirect('addactivities')
    else:
        form = FinancialInfoForm(instance=application)

    context = {
        'form': form,
        'title': "Financial Information",
        'previous_url': reverse('parent_info_view'),
        # 'progress_data': get_form_progress_data(application),
        'progress_data': get_progress_data(request),
        'current_section': 'financial_info'
    }
    return render(request, 'applications/8_financial_info.html', context)

@login_required
def additional_info_view(request):
    application = get_application_for_user(request.user)

    if request.method == "POST":
        form = AdditionalInfoForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()   
            messages.success(request, "Successfully filled and saved your Additional Information!")
            return redirect('writing_section_view')
    else:
        form = AdditionalInfoForm(instance=application)

    context = {
        'form': form,
        'title': "Additional Information",
        'previous_url': reverse('financial_info_view'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'other_inquiries'
    }
    return render(request, 'applications/11_other_inquiries.html', context)

@login_required
def writing_section_view(request):
    application = get_application_for_user(request.user)

    if request.method == "POST":
        form = WritingForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Additional Information!")
            return redirect('files_signature')
    else:
        form = WritingForm(instance=application)

    context = {
        'form': form,
        'title': "Essay Writing",
        'previous_url': reverse('additional_info_view'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'writing'
    }
    return render(request, 'applications/12_essays.html', context)

@login_required
def files_signature(request):
    application = get_application_for_user(request.user)

    if request.method == "POST":
        form = FinalsForm(request.POST, request.FILES, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Additional Information!")
            return redirect('preview_application_view')
    else:
        form = FinalsForm(instance=application)

    context = {
        'form': form,
        'title': "Files Uploading and Signature",
        'previous_url': reverse('additional_info_view'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'files_signature'
    }
    return render(request, 'applications/13_finale.html', context)


@login_required
def addsiblings(request):
    application = get_application_for_user(request.user)
    siblings = Sibling.objects.filter(application=application)
    context = {
        'form': SiblingForm,
        'siblings': siblings,
        'previous_url': reverse('parent_info_view'),
        'next_url': reverse('adddependents'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'siblings'
    }
    return render(request, 'applications/6_addsiblings.html', context)


@login_required
def create_sibling(request):
    if request.method == "POST":
        form = SiblingForm(request.POST)
        if form.is_valid():
            application = get_application_for_user(request.user)
            sibling = form.save(commit=False)
            sibling.application = application
            sibling.save()
            
            # Get all siblings to pass to the template
            siblings = Sibling.objects.filter(application=application)
            context = {
                'siblings': siblings,
                'sibling': sibling  # Also pass the new sibling
            }
            
            # If this is an HTMX request, return just the siblings list
            if request.headers.get('HX-Request'):
                return render(request, 'partials/siblings_list.html', context)
            
            messages.success(request, "Sibling added successfully!")
            return redirect('addsiblings')
    else:
        form = SiblingForm()

    return render(request, 'partials/siblings.html', {'form': form})


@login_required
def update_sibling(request, sibling_id):
    sibling = get_object_or_404(Sibling, id=sibling_id)
    
    if request.method == 'POST':
        form = SiblingForm(request.POST, instance=sibling)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('addsiblings')
    else:
        form = SiblingForm(instance=sibling)
    context = {'form': form}
    return render(request, 'partials/siblings_update.html', context)




@login_required
def delete_sibling(request, sibling_id):
    sibling = get_object_or_404(Sibling, id=sibling_id)
    application = get_application_for_user(request.user)
    if sibling.application == application:
        sibling.delete()
    messages.success(request, "Sibling deleted successfully!")
    return redirect('addsiblings')


@login_required
def adddistinctions(request):
    application = get_application_for_user(request.user)
    
    context = {
        'form': DistinctionForm,
        'distinctions': Distinction.objects.filter(application=application),
        'previous_url': reverse('addactivities'),
        'next_url': reverse('additional_info_view'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'distinctions'
    }
    return render(request, 'applications/10_adddistinctions.html', context)


@login_required
def create_distinction(request):
    if request.method == "POST":
        form = DistinctionForm(request.POST)
        if form.is_valid():
            application = get_application_for_user(request.user)
            distinction = form.save(commit=False)
            distinction.application = application
            distinction.save()  
            context = {'distinction': distinction}
            return render(request, 'partials/distinctions_list.html', context)
    else:
        form = DistinctionForm()

    return render(request, 'partials/distinctions.html', {'form': form})


@login_required
def update_distinction(request, distinction_id):
    distinction = get_object_or_404(Distinction, id=distinction_id)
    
    if request.method == 'POST':
        form = DistinctionForm(request.POST, instance=distinction)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('adddistinctions')
    else:
        form = DistinctionForm(instance=distinction)
    context = {'form': form}
    return render(request, 'partials/distinctions_update.html', context)


@login_required
def delete_distinction(request, distinction_id):
    distinction = get_object_or_404(Distinction, id=distinction_id)
    application = get_application_for_user(request.user)
    if distinction.application == application:
        distinction.delete()
    messages.success(request, "Distinction deleted successfully!")
    return redirect('adddistinctions')

@login_required
def adddependents(request):
    application = get_application_for_user(request.user)
    
    context = {
        'form': DependentForm,
        'dependents': Dependent.objects.filter(application=application),
        'previous_url': reverse('addsiblings'),
        'next_url': reverse('financial_info_view'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'dependents'
    }
    return render(request, 'applications/7_adddependents.html', context)


@login_required
def create_dependent(request):
    if request.method == "POST":
        form = DependentForm(request.POST)
        if form.is_valid():
            application = get_application_for_user(request.user)
            dependent = form.save(commit=False)
            dependent.application = application
            dependent.save()  
            context = {'dependent': dependent}
            return render(request, 'partials/dependents_list.html', context)
    else:
        form = DependentForm()

    return render(request, 'partials/dependents.html', {'form': form})

@login_required
def update_dependent(request, dependent_id):
    dependent = get_object_or_404(Dependent, id=dependent_id)
    
    if request.method == 'POST':
        form = DependentForm(request.POST, instance=dependent)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('adddependents')
    else:
        form = DependentForm(instance=dependent)
    context = {'form': form}
    return render(request, 'partials/dependents_update.html', context)

@login_required
def delete_dependent(request, dependent_id):
    dependent = get_object_or_404(Dependent, id=dependent_id)
    application = get_application_for_user(request.user)
    if dependent.application == application:
        dependent.delete()
    messages.success(request, "Dependent deleted successfully!")
    return redirect('adddependents')


@login_required
def addactivities(request):
    application = get_application_for_user(request.user)
    
    context = {
        'form': ActivityForm,
        'activities': Activity.objects.filter(application=application),
        'previous_url': reverse('financial_info_view'),
        'next_url': reverse('adddistinctions'),
        'progress_data': get_form_progress_data(application),
        'current_section': 'activities'
    }
    return render(request, 'applications/9_addactivities.html', context)

@login_required
def create_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            application = get_application_for_user(request.user)
            activity = form.save(commit=False)
            activity.application = application
            activity.save()  
            context = {'activity': activity}
            return render(request, 'partials/activities_list.html', context)
    else:
        form = ActivityForm()

    return render(request, 'partials/activities.html', {'form': form})


@login_required
def update_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity) 
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('addactivities')
    else:
        form = ActivityForm(instance=activity)
    context = {'form': form}
    return render(request, 'partials/activities_update.html', context)


@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    application = get_application_for_user(request.user)
    if activity.application == application:
        activity.delete()
    messages.success(request, "Activity deleted successfully!")
    return redirect('addactivities')


@login_required
def preview_application_view(request):
    application = get_application_for_user(request.user)
    
    if request.method == "POST":
        application.submitted = True
        application.save()
        messages.success(request, "Application submitted successfully!")
        return redirect('application_submitted_view')

    context = {
        'application': application,
        'title': "Preview Your Application",
        'progress_data': get_form_progress_data(application),
        'current_section': 'preview'
    }
    return render(request, 'applications/14_preview.html', context)


def application_submitted_view(request):
    return render(request, 'applications/application_submitted.html')

# def application_submitted_view(request):
#     application = get_application_for_user(request.user)
#     context = {
#         'application': application
#     }
#     return render(request, 'applications/application_submitted.html', context)

@login_required
@user_passes_test(is_staff_user)
def view_all_applications(request):
    applications = Application.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'applications/view_all_applications.html', context)


def preview_application_viewo(request, user_id):
    user = get_object_or_404(User, id=user_id)
    application = get_application_for_user(user)
    context = {
        'application': application,
        'title': "Preview Your Application",
        'progress_data': get_form_progress_data(application),
        'current_section': 'preview'
    }
    return render(request, 'applications/previewo.html', context)



# def custom_404_view(request, exception):
#     context = {
#         'title': "404 ERROR",
#         'message': "Sorry, the page you are looking for does not exist. Below are some useful links:"
#     }
#     return render(request, 'applications/404.html', context)