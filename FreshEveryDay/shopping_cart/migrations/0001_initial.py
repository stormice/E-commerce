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
            options={
                'db_table': 'CartInfo',
            },
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
                ('gunit', models.CharField(max_length=8)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'GoodsInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('goods', models.ForeignKey(to='shopping_cart.GoodsInfo')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otime', models.DateTimeField()),
                ('ototal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('state', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'TypeInfo',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100, null=True, blank=True)),
                ('uphone', models.CharField(max_length=11)),
                ('ucode', models.CharField(max_length=6)),
                ('ustaue', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'UserAddress',
            },
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
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='shopping_cart.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(to='shopping_cart.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='shopping_cart.OrderInfo'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='shopping_cart.TypeInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='goods',
            field=models.ForeignKey(to='shopping_cart.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(to='shopping_cart.UserInfo'),
        ),
    ]
