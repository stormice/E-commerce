from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.one_order),
    url(r'^pay_order/$',views.pay_order),
    url(r'^commit_order/$',views.commit_order),
    url(r'^user_order/(\d*)$',views.user_order),
   # url(r'^user_order/total_order/$',views.total_order),
    url(r'^FreshCart/$',views.cart_order),
    url(r'^FreshCart/pay_cart_order/$',views.pay_cart_order),
    url(r'^FreshCart/pay_cart_order2/$',views.pay_cart_order2),
    url(r'^FreshCart/commit_order2/$',views.commit_order2),
    url(r'^FreshCart/user_order/(\d*)$',views.user_order),
   # url(r'^FreshCart/user_order/total_order/$',views.total_order),
   # url(r'^FreshCart/user_order/total_page/(\d*)$',views.total_page),
]