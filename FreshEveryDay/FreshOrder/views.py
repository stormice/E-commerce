#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse
from datetime import datetime

#商品详情页面点击"立即购买"即跳转到"提交订单"页面
def one_order(request):
    gid=12
    gcount=4
    userid = 3
    uid=UserInfo.objects.get(pk=userid)

    list=GoodsInfo.objects.get(pk=gid)

    orderinfo=OrderInfo()
    orderinfo.ototal=list.gprice*gcount
    orderinfo.state=False
    orderinfo.user=uid
    orderinfo.save()

    orderdetail = OrderDetailInfo()
    orderdetail.count=gcount
    orderdetail.price=list.gprice
    orderdetail.goods=list
    orderdetail.order=orderinfo
    orderdetail.save()

    return render(request, 'FreshOrder/place_order.html')

#点击"立即购买"触发"提交订单"页面js请求URL执行此视图生成订单
def pay_order(request):
    gid=12
    list=OrderDetailInfo.objects.get(goods_id=gid)
    totalprice=list.price*list.count
    totalsum=totalprice+10
    list_temp=[]
    list_temp.append([list.goods.gpic,list.goods.gtitle,list.price,list.count,totalprice,totalsum])
    return JsonResponse({'data':list_temp})


#提交订单更改订单状态
def commit_order(request):
    gid=12
    orderdetail=OrderDetailInfo.objects.get(goods_id=gid)
    oid=orderdetail.order.pk
    orderinfo=OrderInfo.objects.get(pk=oid)
    orderinfo.state=True
    orderinfo.save()
    return render(request)

#提交订单跳转到用户中心"全部订单页面"
def user_order(request):
    return render(request,'FreshOrder/user_center_order.html')


#从提交订单页面跳转到用户中心"全部订单"显示订单信息
def total_order(request):
    userid=3
    orderinfo=OrderInfo.objects.filter(user_id=userid)
    listdetail=[]
    for lin in orderinfo:
        oid=lin.id
        orderdetail=OrderDetailInfo.objects.filter(order_id=oid)
        for lid in orderdetail:
            listdetail.append([lin.otime,lin.id,lin.state,lin.ototal,lid.goods.gpic,lid.goods.gtitle,lid.count,lid.price])
    return JsonResponse({'data':listdetail})

#购物车页面点击“结算”按钮跳转至“提交订单”页面
def cart_order(request):
    return render(request,'FreshOrder/place_order_cart.html')

