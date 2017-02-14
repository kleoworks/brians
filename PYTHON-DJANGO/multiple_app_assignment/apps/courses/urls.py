from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^add_course$', views.create, name='create' ),
    url(r'^users_courses$', views.users_courses, name='users_courses'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name='destroy')

]
