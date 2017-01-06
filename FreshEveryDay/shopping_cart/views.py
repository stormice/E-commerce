#coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import *

def cart(request):
    # uname = request.user
    user = CartInfo.objects.filter(user__pk=1)
    context = {'user': user, 'pageName': '购物车'}
    return render(request, 'shopping_cart/cart.html', context)

def delete(request):
    cartId = request.GET['delUser']
    cartinfo = CartInfo.objects.get(pk=cartId)
    cartinfo.delete()
    return JsonResponse({})

def change(request):
    count = request.GET['changeCount']
    cartId = request.GET['changeId']
    cartinfo = CartInfo.objects.get(pk=cartId)
    cartinfo.count = count
    cartinfo.save()
    return JsonResponse({})
