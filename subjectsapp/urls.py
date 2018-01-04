from django.conf.urls import include, url

from subjectsapp import views


urlpatterns =[
    url(r'^allsubjects/$', views.subjectlist, name="subjectlist"),
    url(r'^addsubject/$', views.add_subject, name="add_subject"),

 ]