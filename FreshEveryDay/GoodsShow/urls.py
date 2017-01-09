from django.conf.urls import  url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list(\d*)/(\d*)$', views.list),
    url(r'^detail(\d+)', views.detail),
    url(r'^getsession/$',views.getsession),
    url(r'^send/$',views.send),
]