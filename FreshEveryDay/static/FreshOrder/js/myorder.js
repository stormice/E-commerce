/**
 * Created by anchir on 2017/1/6.
 */

$(function () {
    $.get('total_order/',function (dic) {
        $.each(dic.data,function (index,item) {
            if(item[2]==1){
                item[2]='已支付';
                item[8]='已付款';
                item[9]='查看物流';
            }
            else{
                item[2]='未支付';
                item[8]='待付款';
                item[9]='去付款';
            }
            $('#total_order').append('<ul class="order_list_th w978 clearfix">'+'<li class="col01">'+item[0]+'</li>'+'<li class="col02">订单号：'+item[1]+'</li>'+'<li class="col02 stress">'+item[2]+'</li></ul>'+'<table class="order_list_table w980">'+'<tbody>'+'<tr>'+'<td width="55%">'+'<ul class="order_goods_list clearfix">'+'<li class="col01"><img src="'+item[4]+'"></li>'+'<li class="col02">'+item[5]+'<em>11.80元/500g</em></li>'+'<li class="col03">'+item[6]+'</li>'+'<li class="col04">'+item[7]+'</li></ul>'+'</td>'+'<td width="15%">'+item[3]+'元</td>'+'<td width="15%">'+item[8]+'</td>'+'<td width="15%"><a href="#" class="oper_btn">'+item[9]+'</a></td>'+'</tr>'+'</tbody>'+'</table>')

        })
        /**
        $('#total_order').append('<div class="pagenation">'+'<a href="#">上一页</a>'+'<a href="#" class="active">1</a>'+'<a href="#">2</a>'+'<a href="#">3</a>'+'<a href="#">4</a>'+'<a href="#">5</a>'+'<a href="#">下一页></a></div>')
        */
    });

});

/**
 $('#total_order').append('<ul class="order_list_th w978 clearfix">'+'<li class="col01">'+item[0]+'</li>'+'<li class="col02">订单号：'+item[1]+'</li>'+'<li class="col02 stress">'+item[2]+'</li></ul>'+'<table class="order_list_table w980">'+'<tbody>'+'<tr>'+'<td width="55%">'+'<ul class="order_goods_list clearfix">'+'<li class="col01"><img src="'+item[4]+'"></li>'+'<li class="col02">'+item[5]+'<em>11.80元/500g</em></li>'+'<li class="col03">'+item[6]+'</li>'+'<li class="col04">'+item[7]+'</li></ul>'+'</td>'+'<td width="15%">'+item[3]+'元</td>'+'<td width="15%">'+item[8]+'</td>'+'<td width="15%"><a href="#" class="oper_btn">'+item[9]+'</a></td>'+'</tr>'+'</tbody>'+'</table>')
*/