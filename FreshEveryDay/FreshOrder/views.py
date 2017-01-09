#coding=utf-8
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from models import *
import json
from django.http import JsonResponse,HttpResponse


#商品详情页面点击"立即购买"即跳转到"提交订单"页面并保存订单信息
def one_order(request):
    #gid=request.GET['']
    gid=5
    #gcount=request.GET['']
    gcount=3
    #userid=request.session['uname']
    userid = 3
    useradd=UserAddress.objects.filter(user_id=userid,ustaue=1)
    userlist=[]
    for u in useradd:
        userlist.append({'uadd':u.uaddress,'uname':u.userName,'uphone':u.uphone})
    list=GoodsInfo.objects.get(pk=gid)
    totalprice=list.gprice*gcount
    totalsum = totalprice + 10
    listtemp=[]
    listtemp.append({'gpic':list.gpic,'gtitle':list.gtitle,'gprice':list.gprice,'gcount':gcount,'totalprice':totalprice,'totalsum':totalsum})
    context={'pageName':'提交订单','userlist':userlist,'goodslist':listtemp,'gid':gid,'gcount':gcount,'userid':userid,'totalsum':totalsum}

    return render(request, 'FreshOrder/place_order.html',context)



#提交订单更改订单状态
def commit_order(request):
    gid = request.GET['gid']
    gcount=request.GET['gcount']
    userid=request.GET['userid']
    totalsum=request.GET['totalsum']
    uid = UserInfo.objects.get(pk=userid)
    list = GoodsInfo.objects.get(pk=gid)

    orderinfo = OrderInfo()
    orderinfo.ototal=totalsum
    orderinfo.state=True
    orderinfo.user=uid
    orderinfo.save()

    orderdetail = OrderDetailInfo()
    orderdetail.count=gcount
    orderdetail.price=list.gprice
    orderdetail.goods=list
    orderdetail.order=orderinfo
    orderdetail.save()

    return redirect('/FreshOrder/user_order')

#提交订单跳转到用户中心"全部订单页面"
def user_order(request,pindex):
    if pindex=='':
        pindex=1

    # userid=request.session['uname']
    userid=3
    orderinfo=OrderInfo.objects.filter(user_id=userid)
    paginator = Paginator(orderinfo, 2)
    page = paginator.page(int(pindex))
    listdetail = []

    for lin in orderinfo:
        oid = lin.id
        orderdetail = OrderDetailInfo.objects.filter(order_id=oid)
        for lid in orderdetail:
            listdetail.append({'orderId':lid.order_id,'gpic':lid.goods.gpic, 'gtitle':lid.goods.gtitle, 'gcount':lid.count, 'gprice':lid.price})
    context = {'pageName':'用户中心','page': page,'orderlist':listdetail}
    return render(request,'FreshOrder/user_center_order.html',context)


#购物车页面点击“结算”按钮跳转至“提交订单”页面并保存订单信息
def cart_order(request):
    # userid=request.session['uname']
    userid=3
    useradd=UserAddress.objects.filter(user_id=userid,ustaue=1)
    userlist=[]
    for u in useradd:
        userlist.append({'uadd':u.uaddress,'uname':u.userName,'uphone':u.uphone})
    #cartid=request.GET.getlist('cartid')
    #cartid=json.loads(cartid[0])
    cartid=[5,6,7]
    cartlist=CartInfo.objects.filter(pk__in=cartid)
    total=0
    totalcount=0
    goodslist=[]
    num=0
    for cart in cartlist:
        num+=1
        totalcount += cart.count
        totalprice=cart.goods.gprice*cart.count
        goodslist.append({'num':num,'gpic':cart.goods.gpic,'gtitle':cart.goods.gtitle,'gprice':cart.goods.gprice,'gcount':cart.count,'totalprice':totalprice})
        total+=totalprice

    totalsum=total+10

    context={'pageName':'提交订单','userlist':userlist,'goodslist':goodslist,'totalcount':totalcount,'total':total,'totalsum':totalsum,'cartid':cartid,'userid':userid}

    return render(request,'FreshOrder/place_order_cart.html',context)

#提交购物车页面的订单并之后删除购物车里的商品
def commit_order2(request):

    cartid=request.GET.getlist('cartid')
    cartid=json.loads(cartid[0])
    cartlist=CartInfo.objects.filter(pk__in=cartid)
    totalprice=0
    for n in cartlist:
        totalprice+=n.goods.gprice*n.count

    userid = request.GET['userid']
    uid=UserInfo.objects.get(pk=userid)

    orderinfo=OrderInfo()
    orderinfo.ototal=totalprice
    orderinfo.state=True
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


    return redirect('/FreshOrder/user_order')