#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse
import hashlib
def register(request):
    return render(request,'usermode/register.html')
def register_handle(request):
    uname=request.POST['user_name']
    upwd = request.POST['pwd']
    uemail = request.POST['email']

    a=hashlib.sha1()
    a.update(upwd)

    userinfo1=UserInfo()
    userinfo1.uname=uname
    userinfo1.upwd=a.hexdigest()
    userinfo1.uemail=uemail
    userinfo1.save()

    request.session['uname'] = uname
    request.session.set_expiry(0)
    return redirect('/usermode/user_center_info/')
def register_checkname(request):
    uname=request.GET['uname']
    a=UserInfo.objects.filter(isDelete=False,uname=uname)
    if a.count()==0:
        b='yes'
    else:
        b='no'
    return JsonResponse({'isOnly':b})
def user_center_info(request):
    name=request.session.get('uname',None)
    print(name)
    if name!=None:
        a=UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists()==True:
            context={'statu':'login','user':a[0]}
            return render(request, 'usermode/user_center_info.html', context)
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')

def user_center_site(request):
    name = request.session.get('uname', None)
    if name!=None:
        a=UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists()==True:
            userAddr=a[0].useraddress_set
            defaultAddr=userAddr.filter(ustaue=True)
            addrList = userAddr.all()
            # print(defaultAddr)
            if addrList.count()!=0:
                # print(defaultAddr.count())
                if defaultAddr.count() == 0:
                    defaultAddress = 'no'
                else:
                    defaultAddress = defaultAddr[0]

                context={'statu':'login','user':a[0],'useraddress':addrList,'defaultAddress':defaultAddress}
                return render(request, 'usermode/user_center_site.html', context)
            else:
                return redirect('/usermode/user_center_site1/')
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')
def user_center_site1(request):
    name = request.session.get('uname', None)
    if name != None:
        context={'uname':name}
        return render(request, 'usermode/user_center_site1.html', context)
    else:
        return redirect('/GoodsShow/')
def addr_save(request):
    name = request.session.get('uname',None)
    if name !=None:
        a = UserInfo.objects.filter(isDelete=False, uname=name)
        if a.exists() == True:
            uname = request.POST['username']
            uaddr = request.POST['useraddress']
            ucode = request.POST['ucode']
            uphone= request.POST['uphone']
            user_id = a[0].id

            useraddr=UserAddress()
            useraddr.userName=uname
            useraddr.uaddress=uaddr
            useraddr.uphone=uphone
            useraddr.ucode=ucode
            useraddr.user_id=user_id
            useraddr.ustaue= False
            useraddr.save()
            return redirect('/usermode/user_center_site/')
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')
def changeDefaultAddr(request):
    id1=request.GET['id1']
    name = request.session.get('uname', None)
    if name != None:
        a = UserInfo.objects.filter(isDelete=False, uname=name)
        if a.exists() == True:
            userAddr = a[0].useraddress_set
            addrList = userAddr.all()
            for x in addrList:
                x.ustaue=False
                if x.id==int(id1):
                    x.ustaue = True
                    b=x
                x.save()
            return JsonResponse({'name':b.userName,'addr':b.uaddress,'tel':b.uphone})
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')
def login(request):
    return render(request,'usermode/login.html')
def login_check(request):
    name=request.POST['username']
    pwd=request.POST['pwd']

    a = hashlib.sha1()
    a.update(pwd)
    a=a.hexdigest()

    list1=UserInfo.objects.filter(uname=name,isDelete=False)
    if list1[0].upwd==a:
        request.session['uname'] = name
        request.session.set_expiry(0)
        return redirect('/GoodsShow/')
    else:
        context = {'login': 'error'}
        return render(request,'usermode/login.html',context)
def exit(request):
    if request.session.has_key('uname'):
        del request.session['uname']
    return redirect('/GoodsShow/')



