from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_checkname/', views.register_checkname),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^user_center_site1/$', views.user_center_site1),
    url(r'^addr_save/$', views.addr_save),
    url(r'^changeDefaultAddr/$', views.changeDefaultAddr),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^exchangelogin/$', views.exchangelogin),
    url(r'^exit/$', views.exit),
    url(r'^forgetpwd/$', views.forgetpwd),
    url(r'^forgetpwd_handle/$', views.forgetpwd_handle),
    url(r'^resetpwd_handle/$', views.resetpwd_handle),
    url(r'^getshi/(\d+)/$', views.getshi),
]