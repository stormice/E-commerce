#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import *
from django.db.models import *
from django.core.paginator import  *


# Create your views here.
def index(request):
    listGoods=[]
    i=0
    while i <6:
        listSrc = GoodsInfo.objects.filter(gtype_id=i+1).order_by('-gprice')[0:4] #.aggregate(Max('gprice')))#order_by('-gprice')


        listDst=[]
        for item in listSrc:

            listDst.append({'id':item.id, 'gtitle':item.gtitle, 'gprice':item.gprice, 'gpic':item.gpic})

        typename = item.gtype.title

        # listGoods[i]:{'type':typename, 'data':[]}
        dicTemp = {'type':typename, 'data':listDst}
        listGoods.append(dicTemp)
        i+=1

    #01水果
    #02海鲜水产
    #03猪牛羊肉
    #04禽类蛋品
    #05新鲜蔬菜
    #06速冻食品

    context = {'listData': listGoods}
    return render(request, 'GoodsShow/index.html',context)


def list(request, typeId, pageId):
    #列表展示部分
    if typeId is None:
        typeId = '1'
    if pageId is None:
        typeId = '1'
    listSrc = GoodsInfo.objects.filter(gtype_id = int(typeId)).order_by('-gprice')

    paginator =Paginator(listSrc,15)
    page=paginator.page(int(pageId))

    #推荐商品部分，取id最大的两个
    listRec_R =GoodsInfo.objects.filter(gtype_id = int(typeId)).order_by('-id')[0:2]

    # typeTitle = TypeInfo.objects.get(pk=int(typeId)).title

    context={'page':page, 'Rec':listRec_R, 'typeId':int(typeId)}
    return render(request,  'GoodsShow/list.html',context)



def detail(request, goodsId):
    goods= GoodsInfo.objects.get(pk = int(goodsId) )
    typeId= goods.gtype_id


    # 推荐商品部分，取id最大的两个
    listRec_R = GoodsInfo.objects.filter(gtype_id = typeId).order_by('-id')[0:2]

    # typeTitle = goods.gtype.title

    context={'goods':goods, 'Rec':listRec_R}
    return render(request,  'GoodsShow/detail.html', context)

def getsession(request):
    # request.session['uname'] = '大美人'
    request.session.flush()
    uname = request.session.get('uname')

    return JsonResponse({'uname': uname})
