#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import *
from django.db.models import *


# Create your views here.
def index(request):
    listGoods=[[]]
    i=0
    # while i <6:
    listTemp=[]
    listTemp = GoodsInfo.objects.filter(gtype_id=i+1).order_by('-gprice')#.aggregate(Max('gprice')))#order_by('-gprice')
    for item in listTemp:
        listGoods[i].append({'gtitle':item.gtitle, 'gprice':item.gprice, 'gpic':item.gpic})


    context = {'list0': listGoods[0]}
        # i+=1
    #01水果
    #02海鲜水产

    #03猪牛羊肉

    #04禽类蛋品

    #05新鲜蔬菜

    #06速冻食品
    # return JsonResponse({'data':listGoods[0]})
    return render(request, 'GoodsShow/index.html',context)
