from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index), # show user registration and login
    url(r'^users$', views.users), # register new user
    url(r'^users/login$', views.login), # login user
    url(r'^success$', views.success) # upon successful login or registration of new user

]
