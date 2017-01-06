#encoding=utf-8
from django.shortcuts import render
from django.http import *
def test(request):
    return render(request, "Adm_Sr_Mod/test.html")
def search(request):
    return render(request, "Adm_Sr_Mod/search.html")
def getsession(request):
    uname = request.session.get('uname')
    return JsonResponse({'uname': uname})

