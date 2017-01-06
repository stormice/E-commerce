from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^delete$', views.delete),
    url(r'^change$', views.change),
]