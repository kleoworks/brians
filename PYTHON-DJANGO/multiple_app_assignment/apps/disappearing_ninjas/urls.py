from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^$', views.show_all, name="show_all"),
    url(r'^(?P<color>[a-z]+)$', views.show_one, name="show_one" ),
]
