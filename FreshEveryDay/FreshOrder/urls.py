from django.conf.urls import url
import views

urlpatterns=[
    url(r'^FreshOrder/$',views.one_order),
    url(r'^FreshOrder/pay_order/$',views.pay_order),
    url(r'^FreshOrder/commit_order/$',views.commit_order),
    url(r'^FreshOrder/user_order/$',views.user_order),
    url(r'^FreshOrder/user_order/total_order/$',views.total_order),
    url(r'^FreshCart/$',views.cart_order),
]