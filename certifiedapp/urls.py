from django.conf.urls import include, url

from certifiedapp import views

urlpatterns =[
    url(r'^login/$', views.certifiedapphome, name="certifiedapphome"),

 ]