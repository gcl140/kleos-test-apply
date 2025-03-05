from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.urls import reverse
from applications.views import intro_view
from applications.models import Application
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from .forms import UserRegistrationForm
from .forms import CustomUserForm
from .models import CustomUser
import datetime
import logging
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

# from resources.models import Resource

User = get_user_model()

# Register view: Handles user registration and sending activation email
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
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
                request, f"Dear {user.first_name}, please confirm your email to complete registration.")
            return redirect('homepage')  # Redirect to login page
    else:
        form = UserRegistrationForm()

    return render(request, 'yuzzaz/register.html', {'form': form})


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


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(email=username).first()
        if user is not None and user.check_password(password):
            auth_login(request, user)
            messages.success(request, "You have successfully logged in.")
            application = Application.objects.filter(user=user).first()
            if application and application.submitted:
                user.is_active = False  # Restrict user from modifying the application
                user.save()
                return redirect('application_submitted_view')
            return redirect('intro_view')
        else:
            messages.error(request, "Invalid credentials, please try again.")

    return render(request, 'yuzzaz/login.html')

def homepage(request):
        return render(request, 'yuzzaz/homepage.html')


@login_required
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('dashboard')
    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'yuzzaz/dashboard.html', {
        'user': user,
        'form': form,
    })


def logout(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'update_profile.html', {'form': form})




@login_required
def user_dashboard(request):
    # Calculate progress (example logic: based on completed assignments)
    total_assignments = Assignment.objects.count()
    completed_assignments = Assignment.objects.filter(completed_by=request.user).count()
    progress = (completed_assignments / total_assignments * 100) if total_assignments > 0 else 0

    context = {
        'user': request.user,
        'progress': round(progress, 2),
    }
    return render(request, 'yuzzaz/user-dashboard.html', context)


@login_required
def assignments_view(request):
    assignments = Assignment.objects.filter(assigned_to=request.user)
    return render(request, 'assignments.html', {'assignments': assignments})

@login_required
def exams_view(request):
    exams = Exam.objects.filter(participants=request.user)
    return render(request, 'exams.html', {'exams': exams})

@login_required
def notes_view(request):
    # Assuming you have a CounselorNotes model
    notes = CounselorNotes.objects.filter(student=request.user)
    return render(request, 'notes.html', {'notes': notes})

@login_required
def resources_view(request):
    resources = Resource.objects.all()  # Or filter based on student type
    return render(request, 'resources.html', {'resources': resources})


# Custom decorator to ensure only logistics workers can access
# def counsellor_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         if not hasattr(request.user, 'coordinator'):
#             return HttpResponseForbidden("You are not authorized to access this page. Go login. ")
#             # return HttpResponseForbidden("You are not authorized to access this page. Go login <a class="nav-link" href="{% url 'login' %}">Login</a> ")
#         return view_func(request, *args, **kwargs)
#     return wrapper

def counsellor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_counsellor:
            return HttpResponseForbidden("You are not authorized to access this page. Please login as a counsellor.")
        return view_func(request, *args, **kwargs)
    return wrapper


# @login_required
# @counsellor_required
# def counsellor_dashboard(request):
#     user = request.user.first_name
#     # orders = Order.objects.all()
#     return render(request, 'yuzzaz/counsellor_dashboard.html', {'user': user})
 

@login_required
@counsellor_required
def counsellor_dashboard(request):
    counselor = request.user.coordinator
    users = CustomUser.objects.all()
    # assignments = Assignment.objects.filter(counselor=counselor)
    return render(request, 'yuzzaz/counsellor_dashboard.html', {
        'user': request.user,
        'users': users,
        # 'assignments': assignments,
    })


@counsellor_required
def students(request):
    counselor = request.user.coordinator
    users = CustomUser.objects.all()
    # assignments = Assignment.objects.filter(counselor=counselor)
    return render(request, 'yuzzaz/students.html', {
        'user': request.user,
        'users': users,
        # 'assignments': assignments,
    })
