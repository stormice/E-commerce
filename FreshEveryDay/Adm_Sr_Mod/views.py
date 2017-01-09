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
def comment(request,idnum):
    comlist=[]
    nr=Gcomment.objects.filter(goods=idnum)
    for temp in nr:
        comlist.append(temp.gcomment)
    print(comlist)
    context={"Nr":comlist}
    return JsonResponse(context)
def commentInfo(request,idnum):
    nr=Gcomment.objects.filter(goods=idnum)
    p=Paginator(nr,10)
    plist=p.page_range
    pagenr=p.page(1)
    context={"plist":plist,"pagenr":pagenr}
    return render(request,"Adm_Sr_Mod/comment.html",context)

