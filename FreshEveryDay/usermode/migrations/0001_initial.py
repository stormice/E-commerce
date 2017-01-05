# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gdesc', models.CharField(max_length=200)),
                ('gdetail', models.CharField(max_length=1000)),
                ('gpic', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('goods', models.ForeignKey(to='usermode.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otime', models.DateTimeField()),
                ('ototal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100, null=True, blank=True)),
                ('uphone', models.CharField(max_length=11)),
                ('ucode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=50)),
                ('uemail', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='usermode.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(to='usermode.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='usermode.OrderInfo'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='usermode.TypeInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='goods',
            field=models.ForeignKey(to='usermode.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(to='usermode.UserInfo'),
        ),
    ]
