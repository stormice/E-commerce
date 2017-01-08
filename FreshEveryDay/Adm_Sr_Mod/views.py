#encoding=utf-8
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import *
from models import *
def test(request):
    return render(request, "Adm_Sr_Mod/test.html")
def search(request):
    return render(request, "Adm_Sr_Mod/search.html")
def getsession(request):
    uname = request.session.get('uname')
    return JsonResponse({'uname': uname})
def comment(request):
    uname=request.session.get("uname")
    if uname==None:
        return render(request,"usermode/login.html")
    else:
        nr=Gcomment.objects.all()
        # num=Gcomment.objects.all().count()
        # Nr=nr[num-2:num-1]
        # context={"Nr":Nr}
        pg=Paginator(nr,2)
        return JsonResponse()
def commentInfo(request):
    nr=Gcomment.objects.all()
    context={"nr":nr}
    return render(request,"Adm_Sr_Mod/comment.html",context)
# def
