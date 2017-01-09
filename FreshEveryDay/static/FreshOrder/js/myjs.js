/**
 * Created by anchir on 2017/1/5.
 */

$(function () {
    $.get('pay_order/',function (dic) {
        $.each(dic.data,function (index,item) {
            $('#pay_list').append('<ul class="goods_list_td clearfix">'+'<li class="col01">1</li>'+'<li class="col02"><img src="'+item[0]+'"></li>'+'<li class="col03">'+item[1]+'</li>'+'<li class="col04">500g</li>'+'<li class="col05">'+item[2]+'元</li>'+'<li class="col06">'+item[3]+'</li>'+'<li class="col07">'+item[4]+'元</li></ul>');
            $('#pay_total').append('<div class="settle_con">'+'<div class="total_goods_count">共<em>'+item[3]+'</em>件商品，总金额<b>'+item[4]+'元</b></div>'+'<div class="transit">运费：<b>10元</b></div>'+'<div class="total_pay">实付款：<b>'+item[5]+'元</b></div>')
        })

    });

});