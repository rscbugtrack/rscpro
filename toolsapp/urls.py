from django.conf.urls import url , include
from toolsapp import views

urlpatterns =[
    url(r'^toolshome/$', views.toolshome,  name='toolshome'),
]