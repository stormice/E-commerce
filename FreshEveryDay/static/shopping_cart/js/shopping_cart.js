/**
 * Created by python on 17-1-4.
 */
$(function () {
    // 计算总数
    function sumCount() {
        var $tcount = 0;
        $('.num_show').each(function () {
            // checkbok复选框
            $tempcheck = $(this).parent().parent().prevAll('.col01').children('input');
            // 判断复选框是否选中
            if ($tempcheck.prop('checked')==true){
                $tcount += parseInt($(this).val())
            }
        });
        return $tcount
    }
    // 计算总价
    function sumPrice() {
        var $tprice = 0;
        $('.subtotal').each(function () {
            // checkbok复选框
            $tempcheck = $(this).prevAll('.col01').children('input');
            // 判断复选框是否选中
            if($tempcheck.prop('checked')==true){
                $tprice += parseFloat($(this).text());
            }
        });
        return $tprice.toFixed(2)
    }

    // 显示小计价格
    $('.subtotal').html(function () {
        return ($(this).prev().children().children('input').val()*parseFloat($(this).prev().prev().text())).toFixed(2)+'元'
    });
    // 显示总数
    $('#total_count em').text(sumCount());
    $('#totalprice  b').text(sumCount());
    // 显示总价
    $('#totalprice em').text(sumPrice());

    // 增加数量
    $('.add').click(function () {
        $(this).next().attr('value', function () {
            return parseInt($(this).val())+1
        });
        // 修改小计价格
        $(this).parent().parent().next('li').html((parseFloat($(this).next().val())*parseFloat($(this).parent().parent().prev().html())).toFixed(2)+'元');
        // 修改总数
        $('#total_count em').text(sumCount());
        $('#totalprice  b').text(sumCount());
        // 修改总价
        $('#totalprice em').html(sumPrice());
        // 修改数据库中的数量
        $count = $(this).next().val();
        $cart_id = $(this).parent().parent().prevAll('.cart_id').text()
        $.get('/shopping_cart/change', {'changeId': $cart_id, 'changeCount': $count})
    });

    // 减少数量
    $('.minus').click(function () {
        $(this).prev().attr('value', function () {
            if ($(this).val()>1)
                {return parseInt($(this).val()-1)}
        });
        // 修改小计价格
        $(this).parent().parent().next('li').html((parseInt($(this).prev().val())*parseFloat($(this).parent().parent().prev().html())).toFixed(2)+'元');
        // 修改总数
        $('#total_count em').text(sumCount());
        $('#totalprice  b').text(sumCount());
        // 修改总价
        $('#totalprice em').html(sumPrice());
        // 修改数据库中的数量
        $count = $(this).prev().val();
        $cart_id = $(this).parent().parent().prevAll('.cart_id').text();
        $.get('/shopping_cart/change', {'changeId': $cart_id, 'changeCount': $count})
    });

    // 全选按钮
    $('.settlements .col01 input').change(function () {
        if ($(this).prop('checked')==false){
            $('.cart_list_td .col01 input').prop('checked', false);
        }
        else{
            $('.cart_list_td .col01 input').prop('checked', true);
        }
        // 修改总数
        $('#total_count em').text(sumCount());
        $('#totalprice  b').text(sumCount());
        // 修改总价
        $('#totalprice em').html(sumPrice());

    });

    // 复选框按钮
    $('.cart_list_td .col01 input').change(function () {
        // 修改总数
        $('#total_count em').text(sumCount());
        $('#totalprice  b').text(sumCount());
        // 修改总价
        $('#totalprice em').html(sumPrice());
    });

    // 隐藏购物车id
    $('.cart_id').hide();
    // 删除按钮
    $('.delete').click(function () {
        $delId = $(this).parent().prevAll('.cart_id').text();
        $.get('/shopping_cart/delete',{'delUser':$delId});
        $(this).parent().parent().remove();
        // 修改总数
        $('#total_count em').text(sumCount());
        $('#totalprice  b').text(sumCount());
        // 修改总价
        $('#totalprice em').html(sumPrice());
    });

    // 结算
    $('#settle').click(function () {
        $idList = [];
        // 把选中商品的id加入一个数组中
        $('.cart_list_td .col01 input').each(function () {
            if (($(this).prop('checked'))==true){
                $id = $(this).parent().prev().text();
                $idList.push($id);
            }
        });
        // 判断用户是否选定商品
        if ($idList.length!=0){
            $(this).attr('href',function () {
                return '/FreshOrder/FreshCart/?cartid='+$idList
            });
        }
        else{
            alert('您还没选任何商品')
        }

        // 通过ajax传递数据
        // if ($idList.length!=0){
        //     $.get('/shopping_cart/test',{'idList': $idList})
        // }
        // else{
        //     alert('您还没选任何商品')
        // }
    })

});


