from django.conf.urls import include, url
from django.contrib import admin

# from hc.accounts.views import login as hc_login
# import bugtrackapp

urlpatterns = [
    # url(r'^admin/login/', hc_login, {"show_password": True}),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('bugtrackapp.urls')),
    url(r'^', include('certifiedapp.urls'))
]
