from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^/$', views.index, name="index"), #GET -- retrieve all products
    url(r'^/new$', views.new, name="new"), #GET -- display form to create a new products
    url(r'/products', views.create, name="create"), #POST -- create a new products
    url(r'/(?P<id>\d+)$', views.show, name="show"), #GET -- show specific product
    url(r'/(?P<id>\d+)/edit$', views.edit, name="edit"), #GET -- show form to edit specific product
    url(r'/(?P<id>\d+)/update$', views.update, name="update"), #POST -- update specific product
    url(r'/(?P<id>\d+)/destroy$', views.destroy, name="destroy"), #POST -- delete specific product

]
