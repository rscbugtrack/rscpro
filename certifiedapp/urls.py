from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from certifiedapp import views as core_views

urlpatterns =[
    # url(r'^login/$', auth_views.login,  name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^userdashbord/$', core_views.userdashbord, name='userdashbord'),

]

