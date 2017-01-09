#coding=utf-8
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from models import *
from django.http import JsonResponse
from datetime import datetime

#商品详情页面点击"立即购买"即跳转到"提交订单"页面并保存订单信息
def one_order(request):
    gid=5
    gcount=3
    userid = 1
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

    return render(request, 'FreshOrder/place_order.html',{'pageName':'提交订单'})

#点击"立即购买"触发"提交订单"页面js请求URL执行此视图显示订单详细信息
def pay_order(request):
    gid=5
    list=OrderDetailInfo.objects.get(goods_id=gid)
    totalprice=list.price*list.count
    totalsum=totalprice+10
    list_temp=[]
    list_temp.append([list.goods.gpic,list.goods.gtitle,list.price,list.count,totalprice,totalsum])
    return JsonResponse({'data':list_temp})


#提交订单更改订单状态
def commit_order(request):
    gid=5
    orderdetail=OrderDetailInfo.objects.get(goods_id=gid)
    oid=orderdetail.order.pk
    orderinfo=OrderInfo.objects.get(pk=oid)
    orderinfo.state=True
    orderinfo.save()
    return render(request)

#提交订单跳转到用户中心"全部订单页面"
def user_order(request,pindex):
    if pindex=='':
        pindex=1
    userid=3
    orderinfo=OrderInfo.objects.filter(user_id=userid)
    paginator = Paginator(orderinfo, 3)
    page = paginator.page(int(pindex))
    listdetail = []

    for lin in orderinfo:
        oid = lin.id
        orderdetail = OrderDetailInfo.objects.filter(order_id=oid)
        for lid in orderdetail:
            listdetail.append({'gpic':lid.goods.gpic, 'gtitle':lid.goods.gtitle, 'gcount':lid.count, 'gprice':lid.price})
    context = {'page': page,'orderlist':listdetail}
    return render(request,'FreshOrder/user_center_order.html',context)
    # return render(request,'FreshOrder/user_center_order.html',{'pageName':'用户中心'})


#从提交订单页面跳转到用户中心"全部订单"显示订单信息
# def total_order(request):
#     userid=3
#     orderinfo=OrderInfo.objects.filter(user_id=userid)
#     listdetail=[]
#     paystat=''
#     payaction=''
#     for lin in orderinfo:
#         oid=lin.id
#         orderdetail=OrderDetailInfo.objects.filter(order_id=oid)
#         for lid in orderdetail:
#             listdetail.append([lin.otime,lin.id,lin.state,lin.ototal,lid.goods.gpic,lid.goods.gtitle,lid.count,lid.price,paystat,payaction])
#     return JsonResponse({'data':listdetail})

#全部订单页面实现分页功能
def total_page(request,pindex):
    if pindex=='':
        pindex=1
    userid=3
    orderinfo=OrderInfo.objects.filter(user_id=userid)
    paginator = Paginator(orderinfo, 3)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request,'FreshOrder/user_center_order.html',context)


#购物车页面点击“结算”按钮跳转至“提交订单”页面并保存订单信息
def cart_order(request):
    cartid=[13,14,15,16]
    cartlist=CartInfo.objects.filter(pk__in=cartid)
    totalcount=0
    totalprice=0
    for n in cartlist:
        totalprice+=n.goods.gprice
        totalcount+=n.count
    userid = 3
    uid=UserInfo.objects.get(pk=userid)

    orderinfo=OrderInfo()
    orderinfo.ototal=totalprice*totalcount
    orderinfo.state=False
    orderinfo.user=uid
    orderinfo.save()


    for m in cartlist:
        orderdetail = OrderDetailInfo()
        orderdetail.count=m.count
        orderdetail.price=m.goods.gprice
        orderdetail.goods=m.goods
        orderdetail.order=orderinfo
        orderdetail.save()
    for c in cartlist:
        c.delete()

    return render(request,'FreshOrder/place_order_cart.html',{'pageName':'提交订单'})

#显示购物车页面生成订单的详细信息
def pay_cart_order(request):
    # cartid = [1, 2, 3, 4]
    # cartlist = CartInfo.objects.filter(pk__in=cartid)
    # gidlist=[]
    # for n in cartlist:
    #     gidlist.append(n.goods.id)
    oid=39
    orderinfo=OrderInfo.objects.get(pk=oid)
    orderdetail=OrderDetailInfo.objects.filter(order_id=oid)
    orderlist=[]
    totalcount=0
    num=0
    for m in orderdetail:
        num+=1
        totalcount+=m.count
        totalprice=m.price*m.count
        orderlist.append([m.goods.gpic,m.goods.gtitle,m.price,m.count,totalprice,num])

    return JsonResponse({'data':orderlist})

def pay_cart_order2(request):
    oid=39
    orderinfo=OrderInfo.objects.get(pk=oid)
    orderdetail=OrderDetailInfo.objects.filter(order_id=oid)
    totalcount=0
    for m in orderdetail:
        totalcount+=m.count

    totalsum=orderinfo.ototal+10
    ordertotal = [[totalcount,orderinfo.ototal,totalsum]]

    return JsonResponse({'data':ordertotal})


def commit_order2(request):
    oid=39
    orderinfo=OrderInfo.objects.get(pk=oid)
    orderinfo.state=True
    orderinfo.save()
    return render(request)