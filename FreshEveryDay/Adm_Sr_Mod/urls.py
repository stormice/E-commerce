from django.conf.urls import include, url
import views
from GoodsShow import urls
urlpatterns = [
    url(r"^test$",views.test),
    url(r"^searchtest",views.search),
    url(r"^getsession$",views.getsession),
    url(r"^$",include("GoodsShow.urls")),
    url(r"^comment(\d+)$",views.comment),
    url(r"^commentInfo(\d+)$",views.commentInfo)
]