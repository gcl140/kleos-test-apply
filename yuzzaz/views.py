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
from django.http import HttpResponseForbidden

# from resources.models import Resource

User = get_user_model()

# Register view: Handles user registration and sending activation email
# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False  # Deactivate account until email verification
#             user.save()

#             # Send activation email
#             current_site = get_current_site(request)
#             mail_subject = "Activate your user account"
#             message = render_to_string("yuzzaz/activate_account.html", {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#                 'protocol': 'https' if request.is_secure() else 'http',
#                 'current_year': datetime.datetime.now().year,
#             })
#             email = EmailMessage(mail_subject, message, to=[user.email])
#             email.content_subtype = "html"  # Ensure the email content type is HTML
#             email.send()

#             messages.success(
#                 request, f"Dear {user.first_name}, we have sent an activation link to your email. Please check your email to complete registration.")
#             return redirect('homepage')  # Redirect to login page
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'yuzzaz/register.html', {'form': form})


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
                'current_year': datetime.datetime.now().year,
            })
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.content_subtype = "html"  # Ensure the email content type is HTML
            email.send()

            messages.success(
                request, f"Dear {user.first_name}, we have sent an activation link to your email. Please check your email to complete registration."
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
        return render(request, 'yuzzaz/homepage.html')


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
