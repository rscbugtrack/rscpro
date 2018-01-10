from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from certifiedapp import views as core_views

urlpatterns =[
    # url(r'^login/$', auth_views.login,  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name="logout"),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^change_password/$', core_views.change_password, name="change_password"),
    url(r'^userdashbord/$', core_views.userdashbord, name='userdashbord'),
    url(r'^Test_List/$',core_views.Test_List,name='Test_List'),
    url(r'^Take_Test/$',core_views.Take_Test,name='Take_Test'),
    url(r'^Test_Results/$',core_views.Test_Results,name='Test_Results'),


]

