$(function(){
    $('.site_con select').change(function () {
        var value1=$(this).val();
        // console.log(value1);
        if(value1!='0'){
            $.get('/usermode/changeDefaultAddr/',{id1:value1},function(data){
            $('#site_con_dl dd').html(data.addr+'&nbsp;&nbsp;&nbsp;&nbsp;('+data.name+'&nbsp;收) &nbsp;&nbsp;&nbsp;&nbsp;' +data.tel);
            })
        }
    })
})
