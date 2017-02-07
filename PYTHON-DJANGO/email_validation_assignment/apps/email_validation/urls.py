from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index), # main page, show form to allow user to add email to DB
    url(r'^process$', views.process), # route to validate email
    url(r'^success$', views.success), # display all successfully added emails currently in DB
    url(r'^emails/destroy/(?P<id>\d+)', views.destroy) # used to delete email from DB

]
