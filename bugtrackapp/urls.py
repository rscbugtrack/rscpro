from django.conf.urls import include, url

from bugtrackapp import views


urlpatterns =[
    url(r'^$', views.rschome, name="rschome"),
    url(r'^rscbugtrack/$', views.rscbugtrack, name="rscbugtrack"),
    url(r'^aboutus/$', views.aboutus, name="aboutus"),
    url(r'^ourteam/$', views.ourteam, name="ourteam"),
    url(r'^contactus/$', views.contactus, name="contactus"),

    #url(r'^contact_us/$', views.contactus, name="contactus"),

 ]
