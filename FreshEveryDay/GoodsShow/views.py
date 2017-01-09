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
    if typeId == '' :
        typeId = '1'
    if pageId == '' :
        pageId = '1'
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

    context={'goods':goods, 'Rec':listRec_R, 'goodsId': goodsId}
    return render(request,  'GoodsShow/detail.html', context)

def send(request):
    userName = request.GET['uname']
    goodsId = request.GET['goodsId']
    Count =int(request.GET['num'])

    userInfo = UserInfo.objects.get(uname=userName)
    cartList = CartInfo.objects.filter(user_id=userInfo.id, goods_id=goodsId)
    # print(0)
    if  len(cartList)!=0:
        # print('11')
        cart_0 = CartInfo.objects.get(user_id=userInfo.id, goods_id=goodsId)
        cart_0.count +=Count
        cart_0.save()
        # context={'count': cart_0.count}
        # print(cart_0.count)

    else:
        # print('22')
        cart = CartInfo()
        cart.user_id = userInfo.id
        cart.goods_id =goodsId
        cart.count=Count
        cart.save()
        # print(cart.count)
        # context={'count': cart.count}
    cartSum = CartInfo.objects.filter(user_id=userInfo.id)
    count =0
    for cart in cartSum:
        count += cart.count

    return JsonResponse({'count':count})



def getsession(request):
    request.session['uname'] = 'dada'
    # request.session.flush()
    uname = request.session.get('uname')
    goodsId = GoodsInfo.objects.all()[0].id
    return JsonResponse({'uname': uname, 'goodsId':goodsId})

