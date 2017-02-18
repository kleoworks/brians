from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.popular, name="popular"),
    url(r'^secrets$', views.create, name="create"),
    url(r'^destroy/(?P<secret_id>[\d]+)$', views.destroy, name="destroy"),
    url(r'^like/(?P<secret_id>[\d]+)/$', views.like, name="like")
]
