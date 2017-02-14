"""multiple_app_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    url(r'login_registration/', include('apps.login_registration.urls', namespace="login_registration")),
    url(r'^courses/', include('apps.courses.urls', namespace="courses")),
    url(r'^timedisplay/', include('apps.timedisplay.urls', namespace="timedisplay")),
    url(r'^disappearing_ninjas/', include('apps.disappearing_ninjas.urls', namespace="disappearing_ninjas")),
    url(r'^survey_form/', include('apps.survey_form.urls', namespace="survey_form")),
    url(r'^', include('apps.multiple_apps.urls', namespace="multiple_apps")),

]
