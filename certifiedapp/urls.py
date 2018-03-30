from django.conf.urls import url
from django.contrib.auth import views as auth_views

from certifiedapp import views as core_views

urlpatterns =[
    # url(r'^login/$', auth_views.login,  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name="logout"),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^change_password/$', core_views.change_password, name="change_password"),
    url(r'^userdashbord/$', core_views.userdashbord, name='userdashbord'),
    url(r'^Test_List/$',core_views.test_list,name='Testlist'),
    url(r'^Take_Predict/$',core_views.takepredict,name='Takepredict'),
    url(r'^charts/simple.png$', core_views.simple),
    url(r'^forgot_password/$', core_views.forgot_password, name="forgot_password"),
    url(r'^upload/csv/$', core_views.upload_csv, name='upload_csv'),
    url(r'^student_freetest/$', core_views.student_freetest, name='student_freetest'),
    url(r'^student_test_submit/$', core_views.student_test_submit, name='student_test_submit'),
    url(r'^student_testresult/$', core_views.student_testresult, name='student_testresult'),

]

