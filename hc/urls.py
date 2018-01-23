from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from hc.accounts.views import login as hc_login
# import bugtrackapp

urlpatterns = [
    # url(r'^admin/login/', hc_login, {"show_password": True}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, {'template_name': 'registration/cert_app_login.html'} ,name='login'),
    url(r'login/$', auth_views.login, {'template_name': 'registration/cert_app_login.html'} ,name='login'),

    url(r'^', include('bugtrackapp.urls', namespace="bugtrackapp")),
    url(r'^', include('certifiedapp.urls',namespace="certifiedapp")),
    url(r'^', include('subjectsapp.urls',namespace="subjectapp")),
    url(r'^', include('toolsapp.urls',namespace="toolsapp")),
]
