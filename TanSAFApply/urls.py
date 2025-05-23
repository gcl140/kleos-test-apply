"""
URL configuration for TanSAFApply project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("yuzzaz.urls")),
    path('apply_intern/', include("application_intern.urls")),
    path('apply_cohort/', include("application_cohort.urls")),
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=True)),

]

# # Serve media files in development (only works if DEBUG = True)
# if not settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Serve media files even when DEBUG is False
if not settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
else:
    # Serve media files in development (only works if DEBUG = True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)