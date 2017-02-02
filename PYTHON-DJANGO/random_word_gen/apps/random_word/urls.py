from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^get_random', views.get_random)

]
