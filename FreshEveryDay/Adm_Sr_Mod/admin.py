from django.contrib import admin
from models import *
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["uname", 'uemail',"isDelete"]
    list_filter = ['uname']
    list_per_page = 10
    search_fields=["uname"]
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["user", 'userName', 'uaddress', "uphone","ucode","ustaue"]
    list_per_page = 10
    search_fields=["user__uname","username","uphone"]
@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ["title","isDelete"]
    list_per_page = 10
    search_fields=["title"]
@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ["gtitle","gtype","gprice","gdesc","gdetail","gpic","gunit","isDelete"]
    list_filter = ["gtype"]
    list_per_page = 10
    search_fields=["gtitle","gtype__title"]


@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ["user","goods","count"]
    list_per_page = 10
    search_fields = ["user__uname"]
@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["user","otime","ototal","state"]
    list_per_page = 10
    search_fields = ["user__uname","state","otime"]
@admin.register(OrderDetailInfo)
class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ["order__user"]
@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ["atitle"]
@admin.register(Gcomment)
class GcommentAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ["user__uname","goods__gtitle","gcomment"]

