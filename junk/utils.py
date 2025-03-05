from applications.models import Application

def get_application_for_user(user):
    application, created = Application.objects.get_or_create(user=user)
    return application
