"""
URL configuration for RSNineteen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from core.views import home, contact_us, about, security_services, night_patrolling, facility_management, deployment, \
    training, supervision, recruitment, camera_monitoring

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
path('contact/', contact_us, name='contact'),
path('about/', about, name='about'),
path('security_services/', security_services, name='security_services'),

path('night_patrolling/', night_patrolling, name='night_patrolling'),

path('facility_management/', facility_management, name='facility_management'),

path('deployment/', deployment, name='deployment'),

path('training/', training, name='training'),

path('supervision/', supervision, name='supervision'),

path('recruitment/', recruitment, name='recruitment'),

path('camera_monitoring/', camera_monitoring, name='camera_monitoring'),
]
