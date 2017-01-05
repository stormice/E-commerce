from django.shortcuts import render, redirect
from models import *

def cart(request):
    # uname = request.user
    user = CartInfo.objects.filter(user__pk=1)
    context = {'user': user}
    return render(request, 'shopping_cart/cart.html', context)

def delete(request):
    cartId = request.GET['delUser']
    cartinfo = CartInfo.objects.get(pk=cartId)
    cartinfo.delete()
