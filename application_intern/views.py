from application_cohort.views import get_application_for_cohort, get_form_progress_data
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import IntroForm, GeneralInfoForm, ContactInfoForm, SchoolInfoForm, ParentInfoForm, FinancialInfoForm, AdditionalInfoForm, InternDependentForm, InternDistinctionForm, InternSiblingForm, InternActivityForm, WritingForm, FinalsForm
from .models import ApplicationIntern, InternSibling, InternDependent, InternDistinction, InternActivity
from application_cohort.models import ApplicationCohort
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.generic import UpdateView

User = get_user_model()

def is_staff_user(user):
    return user.is_staff or user.has_perm('applications.view_all_applications')

# def get_application_for_user(user):
def get_application_for_intern(user):
    application, created = ApplicationIntern.objects.get_or_create(user=user)
    if created:
        print("A new intern application instance was created.")
    else:
        print("Retrieved an existing intern application instance.")
    return application

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

def get_intern_form_progress_data(application, request):
    """Get progress data for the form progress bar"""
    application = ApplicationIntern.objects.get(user=request.user)
    completion_status = application.get_completion_status()
    
    progress_data = {
        'intro': {
            'label': 'Introduction',
            'url': reverse('intern_intro_view'),
            'completed': completion_status['intro']
        },
        'general_info': {
            'label': 'General Info',
            'url': reverse('intern_general_info_view'),
            'completed': completion_status['general_info']
        },
        'contact_info': {
            'label': 'Contact Info',
            'url': reverse('intern_contact_info_view'),
            'completed': completion_status['contact_info']
        },
        'school_info': {
            'label': 'School Info',
            'url': reverse('intern_school_info_view'),
            'completed': completion_status['school_info']
        },
        'family_info': {
            'label': 'Family Info',
            'url': reverse('intern_parent_info_view'),
            'completed': completion_status['family_info']
        },
        'siblings': {
            'label': 'Siblings',
            'url': reverse('intern_addsiblings'),
            'completed': completion_status['siblings']
        },
        'dependents': {
            'label': 'Dependents',
            'url': reverse('intern_adddependents'),
            'completed': completion_status['dependents']
        },
        'financial_info': {
            'label': 'Financial Info',
            'url': reverse('intern_financial_info_view'),
            'completed': completion_status['financial_info']
        },
        'activities': {
            'label': 'Activities',
            'url': reverse('intern_addactivities'),
            'completed': completion_status['activities']
        },
        'distinctions': {
            'label': 'Distinctions',
            'url': reverse('intern_adddistinctions'),
            'completed': completion_status['distinctions']
        },
        'other_inquiries': {
            'label': 'Other Inquiries',
            'url': reverse('intern_additional_info_view'),
            'completed': completion_status['other_inquiries']
        },
        'writing': {
            'label': 'Writing',
            'url': reverse('intern_writing_section_view'),
            'completed': completion_status['writing']
        },
        'files_signature': {
            'label': 'Files & Signature',
            'url': reverse('intern_files_signature'),
            'completed': completion_status['files_signature']
        }
    }
    
    return progress_data

class FormMixin:
    """Mixin to add progress data to context"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress_data'] = get_intern_form_progress_data(application=self.object, request=self.request)
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
    
class FinancialInfoView(FormMixin, UpdateView):
    current_section = 'financial_info'
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

class WritingInfoView(FormMixin, UpdateView):
    current_section = 'writing'
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

class SignatureView(FormMixin, UpdateView):
    current_section = 'files_signature'
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_completion_status()
        return response

@login_required
def intro_view(request):
    application = get_application_for_intern(request.user)

    if request.method == "POST":
        form = IntroForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Intro Form!")
            return redirect('intern_general_info_view')
    else:
        form = IntroForm(instance=application)

    context = {
        'form': form,
        'title': "Introduction",
        'previous_url': None,
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'intro'
    }
    return render(request, 'application_intern/1_intro.html', context)

@login_required
def general_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == 'POST':
        form = GeneralInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  
            application.update_completion_status()
            messages.success(request, 'General information updated successfully.')
            return redirect('intern_contact_info_view')
    else:
        form = GeneralInfoForm(instance=application)
    
    context = {
        'form': form,
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'general_info',
        'previous_url': reverse('intern_intro_view')
    }
    return render(request, 'application_intern/2_general_info.html', context)

@login_required
def contact_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):
            application.update_completion_status()
            messages.success(request, 'Contact information updated successfully.')
            return redirect('intern_school_info_view')
    else:
        form = ContactInfoForm(instance=application)
    context = {
        'form': form,
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'contact_info',
        'previous_url': reverse('intern_general_info_view')
    }
    return render(request, 'application_intern/3_contact_info.html', context)

@login_required
def school_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == 'POST':
        form = SchoolInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  
            application.update_completion_status()
            messages.success(request, 'School information updated successfully.')
            return redirect('intern_parent_info_view')
    else:
        form = SchoolInfoForm(instance=application)
    
    context = {
        'form': form,
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'school_info',
        'previous_url': reverse('intern_contact_info_view')
    }
    return render(request, 'application_intern/4_school_info.html', context)

@login_required
def parent_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == 'POST':
        form = ParentInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):  
            application.update_completion_status()
            messages.success(request, 'Parent information updated successfully.')
            return redirect('intern_addsiblings')
    else:
        form = ParentInfoForm(instance=application)
    
    context = {
        'form': form,
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),
        'current_section': 'family_info',
        'previous_url': reverse('intern_school_info_view')
    }
    return render(request, 'application_intern/5_parents_info.html', context)

@login_required
def financial_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == "POST":
        form = FinancialInfoForm(request.POST, instance=application)
        if save_application_data(application, form, request):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Financial Information!")
            return redirect('intern_addactivities')
    else:
        form = FinancialInfoForm(instance=application)

    context = {
        'form': form,
        'title': "Financial Information",
        'previous_url': reverse('intern_parent_info_view'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),
        'current_section': 'financial_info'
    }
    return render(request, 'application_intern/8_financial_info.html', context)

@login_required
def additional_info_view(request):
    application = get_application_for_intern(request.user)

    if request.method == "POST":
        form = AdditionalInfoForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()   
            messages.success(request, "Successfully filled and saved your Additional Information!")
            return redirect('intern_writing_section_view')
    else:
        form = AdditionalInfoForm(instance=application)

    context = {
        'form': form,
        'title': "Additional Information",
        'previous_url': reverse('intern_financial_info_view'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),
        'current_section': 'other_inquiries'
    }
    return render(request, 'application_intern/11_other_inquiries.html', context)

@login_required
def writing_section_view(request):
    application = get_application_for_intern(request.user)

    if request.method == "POST":
        form = WritingForm(request.POST, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your essay responses!")
            return redirect('intern_files_signature')
    else:
        form = WritingForm(instance=application)

    context = {
        'form': form,
        'title': "Essay Writing",
        'previous_url': reverse('intern_additional_info_view'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),
        'current_section': 'writing'
    }
    return render(request, 'application_intern/12_essays.html', context)


@login_required
def files_signature(request):
    application = get_application_for_intern(request.user)

    if request.method == "POST":
        form = FinalsForm(request.POST, request.FILES, instance=application)
        if save_application_data(application, form):
            application.update_completion_status()
            messages.success(request, "Successfully filled and saved your Files & Signature! ")
            return redirect('intern_preview_application_view')
    else:
        form = FinalsForm(instance=application)
    context = {
        'form': form,
        'title': "Files Uploading and Signature",
        'previous_url': reverse('intern_additional_info_view'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'files_signature'
    }
    return render(request, 'application_intern/13_finale.html', context)


@login_required
def addsiblings(request):
    application = get_application_for_intern(request.user)
    siblings = InternSibling.objects.filter(application=application)
    context = {
        'form': InternSiblingForm,
        'siblings': siblings,
        'previous_url': reverse('intern_parent_info_view'),
        'next_url': reverse('intern_adddependents'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'siblings'
    }
    return render(request, 'application_intern/6_addsiblings.html', context)


@login_required
def create_sibling(request):
    if request.method == "POST":
        form = InternSiblingForm(request.POST)
        if form.is_valid():
            application = get_application_for_intern(request.user)
            sibling = form.save(commit=False)
            sibling.application = application
            sibling.save()
            siblings = InternSibling.objects.filter(application=application)
            context = {
                'siblings': siblings,
                'sibling': sibling  
            }
            if request.headers.get('HX-Request'):
                return render(request, 'intern_partials/siblings_list.html', context)
            
            messages.success(request, "Sibling added successfully!")
            return redirect('intern_addsiblings')
    else:
        form = InternSiblingForm()

    return render(request, 'intern_partials/siblings.html', {'form': form})


@login_required
def update_sibling(request, sibling_id):
    sibling = get_object_or_404(InternSibling, id=sibling_id)
    
    if request.method == 'POST':
        form = InternSiblingForm(request.POST, instance=sibling)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('intern_addsiblings')
    else:
        form = InternSiblingForm(instance=sibling)
    context = {'form': form}
    return render(request, 'intern_partials/siblings_update.html', context)




@login_required
def delete_sibling(request, sibling_id):
    sibling = get_object_or_404(InternSibling, id=sibling_id)
    application = get_application_for_intern(request.user)
    if sibling.application == application:
        sibling.delete()
    messages.success(request, "Sibling deleted successfully!")
    return redirect('intern_addsiblings')


@login_required
def adddistinctions(request):
    application = get_application_for_intern(request.user)
    
    context = {
        'form': InternDistinctionForm,
        'distinctions': InternDistinction.objects.filter(application=application),
        'previous_url': reverse('intern_addactivities'),
        'next_url': reverse('intern_additional_info_view'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),   
        'current_section': 'distinctions'
    }
    return render(request, 'application_intern/10_adddistinctions.html', context)


@login_required
def create_distinction(request):
    if request.method == "POST":
        form = InternDistinctionForm(request.POST)
        if form.is_valid():
            application = get_application_for_intern(request.user)
            distinction = form.save(commit=False)
            distinction.application = application
            distinction.save()  
            context = {'distinction': distinction}
            return render(request, 'intern_partials/distinctions_list.html', context)
    else:
        form = InternDistinctionForm()

    return render(request, 'intern_partials/distinctions.html', {'form': form})


@login_required
def update_distinction(request, distinction_id):
    distinction = get_object_or_404(InternDistinction, id=distinction_id)
    
    if request.method == 'POST':
        form = InternDistinctionForm(request.POST, instance=distinction)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('intern_adddistinctions')
    else:
        form = InternDistinctionForm(instance=distinction)
    context = {'form': form}
    return render(request, 'intern_partials/distinctions_update.html', context)


@login_required
def delete_distinction(request, distinction_id):
    distinction = get_object_or_404(InternDistinction, id=distinction_id)
    application = get_application_for_intern(request.user)
    if distinction.application == application:
        distinction.delete()
    messages.success(request, "InternDistinction deleted successfully!")
    return redirect('intern_adddistinctions')

@login_required
def adddependents(request):
    application = get_application_for_intern(request.user)
    
    context = {
        'form': InternDependentForm,
        'dependents': InternDependent.objects.filter(application=application),
        'previous_url': reverse('intern_addsiblings'),
        'next_url': reverse('intern_financial_info_view'),
        
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'dependents'
    }
    return render(request, 'application_intern/7_adddependents.html', context)


@login_required
def create_dependent(request):
    if request.method == "POST":
        form = InternDependentForm(request.POST)
        if form.is_valid():
            application = get_application_for_intern(request.user)
            dependent = form.save(commit=False)
            dependent.application = application
            dependent.save()  
            context = {'dependent': dependent}
            return render(request, 'intern_partials/dependents_list.html', context)
    else:
        form = InternDependentForm()

    return render(request, 'intern_partials/dependents.html', {'form': form})

@login_required
def update_dependent(request, dependent_id):
    dependent = get_object_or_404(InternDependent, id=dependent_id)
    
    if request.method == 'POST':
        form = InternDependentForm(request.POST, instance=dependent)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('intern_adddependents')
    else:
        form = InternDependentForm(instance=dependent)
    context = {'form': form}
    return render(request, 'intern_partials/dependents_update.html', context)

@login_required
def delete_dependent(request, dependent_id):
    dependent = get_object_or_404(InternDependent, id=dependent_id)
    application = get_application_for_intern(request.user)
    if dependent.application == application:
        dependent.delete()
    messages.success(request, "InternDependent deleted successfully!")
    return redirect('intern_adddependents')


@login_required
def addactivities(request):
    application = get_application_for_intern(request.user)
    
    context = {
        'form': InternActivityForm,
        'activities': InternActivity.objects.filter(application=application),
        'previous_url': reverse('intern_financial_info_view'),
        'next_url': reverse('intern_adddistinctions'),
        'application': application,
        'progress_data': get_intern_form_progress_data(application, request),  
        'current_section': 'activities'
    }
    return render(request, 'application_intern/9_addactivities.html', context)

@login_required
def intern_create_activity(request):
    if request.method == "POST":
        form = InternActivityForm(request.POST)
        if form.is_valid():
            application = get_application_for_intern(request.user)
            activity = form.save(commit=False)
            activity.application = application
            activity.save()  
            context = {'activity': activity}
            return render(request, 'intern_partials/activities_list.html', context)
    else:
        form = InternActivityForm()

    return render(request, 'intern_partials/activities.html', {'form': form})


@login_required
def update_activity(request, activity_id):
    activity = get_object_or_404(InternActivity, id=activity_id)
    
    if request.method == 'POST':
        form = InternActivityForm(request.POST, instance=activity) 
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved successfully!")
            return redirect('intern_addactivities')
    else:
        form = InternActivityForm(instance=activity)
    context = {'form': form}
    return render(request, 'intern_partials/activities_update.html', context)


@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(InternActivity, id=activity_id)
    application = get_application_for_intern(request.user)
    if activity.application == application:
        activity.delete()
    messages.success(request, "Activity deleted successfully!")
    return redirect('intern_addactivities')

@login_required
def preview_application_view(request):
    application = get_application_for_intern(request.user)
    
    if request.method == "POST":
        application.submitted = True
        application.save()
        request.user.is_active = False
        request.user.save()
        messages.success(
            request, 
            f"Dear {request.user.first_name}, 🎉🎉 Your application has been submitted successfully! Best of luck! 🤞"
        )
        return redirect('intern_application_submitted_view')

    context = {
        'application': application,
        'title': "Preview Your Application",
        'current_section': 'preview'
    }
    return render(request, 'application_intern/14_preview.html', context)

def application_submitted_view(request):
    return render(request, 'application_intern/application_submitted.html')

@login_required
@user_passes_test(is_staff_user)
def view_all_applications(request):
    cohort_applications = list(ApplicationCohort.objects.all())
    intern_applications = list(ApplicationIntern.objects.all())
    applications = cohort_applications + intern_applications
    context = {
        'applications': applications,
        }
    return render(request, 'application_intern/view_all_applications.html', context)


def preview_application_viewo(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # application = get_application_for_intern(user)
    if user.is_intern:  # Assuming there's an attribute or method that identifies intern users
        application = get_application_for_intern(user)
        # progress_data = get_intern_form_progress_data(application, request)
        siblings = application.application_intern_siblings.all()
        dependents = application.application_intern_dependents.all()
        distinctions = application.application_intern_distinctions.all()
        activities = application.application_intern_activities.all()
    else:  # If not an intern, assume it's a cohort application
        application = get_application_for_cohort(user)
        # progress_data = get_form_progress_data(application, request)
        siblings = application.application_cohort_siblings.all()
        dependents = application.application_cohort_dependents.all()
        distinctions = application.application_cohort_distinctions.all()
        activities = application.application_cohort_activities.all()

    context = {
        'application': application,
        'title': "Preview Your Application",
        'current_section': 'preview',
        'application': application,
        # 'progress_data': progress_data,  
        'siblings': siblings,
        'dependents': dependents,
        'distinctions': distinctions,
        'activities': activities,
    }
    return render(request, 'application_intern/previewo.html', context)
