from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.one_order),
    url(r'^commit_order/$',views.commit_order),
    url(r'^user_order/(\d*)$',views.user_order),
    url(r'^FreshCart/$',views.cart_order),
    url(r'^FreshCart/commit_order2/$',views.commit_order2),
    url(r'^FreshCart/user_order/(\d*)$',views.user_order),
]