from django.conf.urls import url

from bugtrackapp import views


urlpatterns =[
    url(r'^blog_id/(\d+)/', views.blog_id, name="blogid"),
    url(r'^rscbugtrack/$', views.rscbugtrack, name="rscbugtrack"),
    url(r'^aboutus/$', views.aboutus, name="aboutus"),
    url(r'^ourteam/$', views.ourteam, name="ourteam"),
    url(r'^contactus/$', views.contactus, name="contactus"),

    url(r'^home/$', views.rschome, name="rschome"),

 ]
