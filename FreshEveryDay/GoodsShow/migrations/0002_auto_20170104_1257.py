# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoodsShow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cartinfo',
            table='CartInfo',
        ),
        migrations.AlterModelTable(
            name='goodsinfo',
            table='GoodsInfo',
        ),
        migrations.AlterModelTable(
            name='orderdetailinfo',
            table='OrderDetailInfo',
        ),
        migrations.AlterModelTable(
            name='orderinfo',
            table='OrderInfo',
        ),
        migrations.AlterModelTable(
            name='typeinfo',
            table='TypeInfo',
        ),
        migrations.AlterModelTable(
            name='useraddress',
            table='UserAddress',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='UserInfo',
        ),
    ]
