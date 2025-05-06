from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from application_intern.models import ApplicationIntern
from application_cohort.models import ApplicationCohort
# from .models import User, ApplicationIntern, ApplicationCohort
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from .forms import UserRegistrationForm
from .forms import CustomUserForm
import datetime

from django.utils import timezone
from datetime import datetime

from django.http import HttpResponseForbidden

User = get_user_model()


def register(request, user_type):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
            
            # Set user type based on URL parameter
            if user_type == "intern":
                user.is_intern = True
            else:
                user.is_intern = False  # Default to cohort
            
            user.save()

            # Send activation email
            current_site = get_current_site(request)
            mail_subject = "Activate your user account"
            message = render_to_string("yuzzaz/activate_account.html", {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http',
                # 'current_year': datetime.datetime.now().year,
                'current_year': datetime.now().year,

            })
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.content_subtype = "html"  # Ensure the email content type is HTML
            email.send()

            messages.success(
                request, f"Dear {user.first_name}, we have sent an activation link to your email. Please check your email to complete registration (Remember to check your spam too, you can't proceed without that email)."
            )
            return redirect('homepage')  # Redirect to login page
    else:
        form = UserRegistrationForm()

    return render(request, 'yuzzaz/register.html', {'form': form, 'user_type': user_type})


# Activate view: Handles the account activation via the token
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for confirming your email. You can now log in.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid.")
        return redirect('homepage')



def get_application_for_intern(user):
    application, created = ApplicationIntern.objects.get_or_create(user=user)
    if created:
        print("A new Intern pplication instance was created.")
    else:
        print("Retrieved an existing Intern Application instance.")
    return application

def get_application_for_cohort(user):
    application, created = ApplicationCohort.objects.get_or_create(user=user)
    if created:
        print("A new Cohort pplication instance was created.")
    else:
        print("Retrieved an existing Cohort Application instance.")
    return application

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(email=username).first()
        if user is not None and user.check_password(password):
            auth_login(request, user)
            messages.success(request, "You have successfully logged in.")

            # Check if the user is an intern or cohort and create their application instance
            if user.is_intern:
                application = get_application_for_intern(user)
                if application.submitted:
                    return redirect('intern_application_submitted_view')
                return redirect('intern_intro_view')  # Replace with your actual URL name
            else:
                application = get_application_for_cohort(user)
                if application.submitted:
                    return redirect('application_submitted_view')
                return redirect('intro_view')  # Replace with your actual URL name

        else:
            messages.error(request, "Invalid credentials, please try again.")

    return render(request, 'yuzzaz/login.html')


def homepage(request):
    now = timezone.now()
    open_date = timezone.make_aware(datetime(2025, 4, 26))
    close_date = timezone.make_aware(datetime(2025, 6, 26))
    portal_open = open_date <= now < close_date
    return render(request, 'yuzzaz/homepage.html', {
        'portal_open': portal_open
    })


def logout(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

def counsellor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_counsellor:
            return HttpResponseForbidden("You are not authorized to access this page. Please login as a counsellor.")
        return view_func(request, *args, **kwargs)
    return wrapper



@user_passes_test(lambda u: u.is_staff)
def activate_all_users(request):
    inactive_users = User.objects.filter(is_active=False)
    # inactive_users = User.objects.filter(is_active=False, application__submitted=False)
    count = inactive_users.count()

    for user in inactive_users:
        user.is_active = True
        user.save()

    messages.success(request, f"Successfully activated {count} inactive user(s).")
    return redirect('intern_view_all_applications')  # Change to your desired redirect URL
    

@user_passes_test(lambda u: u.is_staff)
@require_POST
def activate_user_by_email(request):
    email = request.POST.get('email')
    user = User.objects.filter(email=email).first()

    if user:
        if user.is_active:
            messages.info(request, f"User '{email}' is already active.")
        else:
            user.is_active = True
            user.save()
            messages.success(request, f"User '{email}' has been activated.")
    else:
        messages.error(request, f"No user found with email '{email}'.")

    return redirect('intern_view_all_applications')





# views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BulkEmailForm
from .models import CustomUser
from django.template.loader import render_to_string


def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def send_custom_email(request):
    if request.method == 'POST':
        form = BulkEmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            heading = form.cleaned_data['heading']
            content = form.cleaned_data['content']
            content1 = form.cleaned_data['content1']
            content2 = form.cleaned_data['content2']
            attachment = form.cleaned_data.get('attachment')
            send_to_all = form.cleaned_data['send_to_all']
            selected_users = form.cleaned_data['selected_users']

            if send_to_all:
                recipients = CustomUser.objects.all()
            else:
                recipients = selected_users

            for user in recipients:
                context = {
                    'full_name': user.get_full_name(),
                    'user': user,
                    'heading': heading,
                    'content': content,
                    'content1': content1,
                    'content2': content2,
                }
                html_content = render_to_string('emails/custom_email.html', context)
                plain_content = strip_tags(html_content)

                email = EmailMultiAlternatives(subject, plain_content, to=[user.email])
                email.attach_alternative(html_content, "text/html")

                if attachment:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)

                email.send()

            messages.success(request, "Emails have been sent successfully!")
            return redirect('intern_view_all_applications')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = BulkEmailForm()

    return render(request, 'emails/send_custom_email.html', {'form': form})
