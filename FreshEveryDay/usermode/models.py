# encoding=utf-8
from django.db import models
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=50)
    uemail=models.CharField(max_length=40)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='UserInfo'
class UserAddress(models.Model):
    user=models.ForeignKey(UserInfo)
    userName=models.CharField(max_length=20)
    uaddress=models.CharField(max_length=100,null=True,blank=True)
    uphone=models.CharField(max_length=11)
    ucode=models.CharField(max_length=6)
    ustaue = models.BooleanField(default=False)
    class Meta:
        db_table='UserAddress'
class TypeInfo(models.Model):
    title=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='TypeInfo'
class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gtype=models.ForeignKey(TypeInfo)
    gprice=models.DecimalField(max_digits=5,decimal_places=2)
    gdesc=models.CharField(max_length=200)
    gdetail=models.CharField(max_length=1000)
    gpic=models.CharField(max_length=200)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='GoodsInfo'
class CartInfo(models.Model):
    user=models.ForeignKey(UserInfo)
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
    class Meta:
        db_table='CartInfo'
class OrderInfo(models.Model):
    otime=models.DateTimeField()
    user=models.ForeignKey(UserInfo)
    ototal=models.DecimalField(max_digits=8,decimal_places=2)
    state=models.BooleanField(default=False)
    class Meta:
        db_table='OrderInfo'
class OrderDetailInfo(models.Model):
    order=models.ForeignKey(OrderInfo)
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        db_table='OrderDetailInfo'