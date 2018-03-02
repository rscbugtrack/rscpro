from django.conf.urls import include, url

from subjectsapp import views


urlpatterns =[
    url(r'^allsubjects/$', views.subjectlist, name="subjectlist"),
    url(r'^addsubject/$', views.add_subject, name="add_subject"),
    url(r'^editsubject/(?P<pk>\d+)$', views.edit_subject, name="editsubject"),
    url(r'^allpapers/$', views.paperslist, name="paperslist"),
    url(r'^addpapers/$', views.add_papers, name="add_papers"),
    url(r'^editpapertype/(?P<pk>\d+)$', views.edit_papertype, name="edit_papertype"),
    url(r'^allquestions/$', views.questionlist, name="questionlist"),
    url(r'^addquestions/$', views.add_questions, name="add_questions"),
    url(r'^editquestiontype/(?P<pk>\d+)$', views.edit_questions, name="edit_questions"),
    url(r'^results/$', views.results, name="results"),

]
