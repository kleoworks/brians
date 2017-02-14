from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'), # show user registration and login
    url(r'^register$', views.register, name='register'), # register new user
    url(r'^login$', views.login, name='login'), # login user
    url(r'^success$', views.success, name='success'), # upon successful login or registration of new user
    url(r'^logout$', views.logout, name='logout') # logout user

]
