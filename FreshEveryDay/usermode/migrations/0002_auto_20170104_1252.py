# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermode', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cartinfo',
            table='cartinfo',
        ),
        migrations.AlterModelTable(
            name='goodsinfo',
            table='goodsinfo',
        ),
        migrations.AlterModelTable(
            name='orderdetailinfo',
            table='orderdetailinfo',
        ),
        migrations.AlterModelTable(
            name='orderinfo',
            table='orderinfo',
        ),
        migrations.AlterModelTable(
            name='typeinfo',
            table='typeinfo',
        ),
        migrations.AlterModelTable(
            name='useraddress',
            table='useraddress',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userinfo',
        ),
    ]
