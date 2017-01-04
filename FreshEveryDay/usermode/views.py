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
    name=request.session.get('uname','未登录')
    if name!='未登录':
        a=UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists()==True:
            context={'statu':'login','user':a[0]}
            return render(request, 'usermode/user_center_info.html', context)
        else:
            del request.session['name']
            return render(request, 'usermode/login.html')
    else:
        return render(request, 'usermode/login.html')

def user_center_site(request):
    name = request.session.get('uname', '未登录')
    if name!='未登录':
        a=UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists()==True:
            context={'statu':'login','user':a[0],'useraddress':a[0].useraddress_set.all()}
            return render(request, 'usermode/user_center_site.html', context)
        else:
            del request.session['name']
            return render(request, 'usermode/login.html')
    else:
        return render(request, 'usermode/login.html')


