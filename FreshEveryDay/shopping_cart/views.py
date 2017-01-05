from django.shortcuts import render
from models import *

def cart(request):
    # uname = request.user
    user = CartInfo.objects.filter(user__pk=1)
    context = {'user': user}
    return render(request, 'shopping_cart/cart.html', context)