$(function(){
	var prevURL=document.referrer
	var isOrder=prevURL.search(/FreshOrder/)
	if(isOrder!=-1){
		$('#common_title2_h3').append('<a class="orderstyle" href="'+prevURL+'">返回订单页</a>')
	}
    $('#address_def').change(function () {
        var value1=$(this).val();
        // console.log(value1);
        if(value1!='0'){
            $.get('/usermode/changeDefaultAddr/',{id1:value1},function(data){
            $('#site_con_dl dd').html(data.addr+'&nbsp;&nbsp;&nbsp;&nbsp;('+data.name+'&nbsp;收) &nbsp;&nbsp;&nbsp;&nbsp;' +data.tel);
            })
        }
    })


    $('#pro').change(function(){
				$('#city').empty().append('<option value="0">请选择市</option>')
				$('#dis').empty().append('<option value="0">请选择县</option>')
				var val=$(this).val();
				if(val==0){
					return;
				}
				$.get('/usermode/getshi/'+val+'/',function(data){
					$city=$('#city')
					$.each(data.list,function(index,item){
					$city.append('<option value="'+item[0]+'">'+item[1]+'</option>')
				})
				})
			})
			$('#city').change(function(){
				$('#dis').empty().append('<option value="0">请选择县</option>');
				var val=$(this).val();
				if(val==0){
					return;
				}
				$.get('/usermode/getshi/'+val+'/',function(data){
					$dis=$('#dis')
					$.each(data.list,function(index,item){
						$dis.append('<option value="'+item[0]+'">'+item[1]+'</option>');
					})
				})
			});

			var error_name = false;
			var error_address = false;
			var error_tel = false;
			var error_code = false;
			$('#username').blur(function(){
				check_username();
			})


			$('#useraddress').blur(function(){
				check_useraddress();
			})


			$('#ucode').blur(function(){
				check_ucode();
			})


			$('#uphone').blur(function(){
				check_uphone();
			})


			function check_username(){
				var value1 = $('#username').val().trim();
				var len=value1.length;
				if(len<2||len>20)
				{
					$('#username').next().html('*请输入2-20个字符的收件人姓名')
					$('#username').next().css('display','inline-block');
					error_name = true;
				}else{
					$('#username').next().hide();
					error_name = false;
				}
			}


			function check_useraddress(){
				var value1 = $('#useraddress').val().trim();
				var len=value1.length;
				if($('#dis').val()=='0'){
					$('#useraddress').next().html('*请选择省、市、区')
					$('#useraddress').next().css('display','inline-block');
					error_address = true;
				}else if(len<5||len>100)
				{
					$('#useraddress').next().html('*请输入5-100个字符的详细收件地址')
					$('#useraddress').next().css('display','inline-block');
					error_address = true;
				}else{
					$('#useraddress').next().hide();
					error_address = false;
				}
			}

			function check_ucode(){
				var re = /^\d{6}$/;

				if(re.test($('#ucode').val().trim()))
				{
					$('#ucode').next().hide();
					error_code = false;
				}
				else
				{
					$('#ucode').next().html('*你输入的邮编格式不正确')
					$('#ucode').next().css('display','inline-block');
					error_code = true;
				}

			}


			function check_uphone(){
				var re = /^1[3|4|5|8][0-9]\d{4,8}$/;

				if(re.test($('#uphone').val().trim()))
				{
					$('#uphone').next().hide();
					error_tel = false;
				}
				else
				{
					$('#uphone').next().html('*请输入11位数的手机号码')
					$('#uphone').next().css('display','inline-block');
					error_tel = true;
				}
			}



			$('.info_submit').click(function(){
				check_username();
				check_useraddress();
				check_ucode();
				check_uphone();

				if(error_name == false && error_address == false &&
error_tel == false && error_code == false)
				{
					var username=$('#username').val();
					var pro=$('#pro').val();
					var city=$('#city').val();
					var dis=$('#dis').val();
					var useraddress=$('#useraddress').val();
					var ucode=$('#ucode').val();
					var uphone=$('#uphone').val();
					$.get('/usermode/addr_save/',{username:username,pro:pro,city:city,dis:dis,useraddress:useraddress,ucode:ucode,uphone:uphone},function(data){
						if(data.success=='ok'){
							$('#username').val('');
							$('#pro').val('0');
							$('#city').val('0');
							$('#dis').val('0');
							$('#useraddress').val('');
							$('#ucode').val('');
							$('#uphone').val('');
							alert('添加成功!');
							updateaddr();
						}
					});
				}
				else
				{
					return false;
				}

			})



	function updateaddr(){
		$.get('/usermode/getuseraddr/',function(data){
			if(data.success=='ok'){
				$('#address_def').empty().append('<option value="0">请选择收货地址</option>');
				$.each(data.addrList,function(index,item){
					$('#address_def').append('<option value="'+item[0]+'">'+item[1]+'&nbsp;&nbsp;&nbsp;&nbsp;('+item[2]+' &nbsp;收) &nbsp;&nbsp;&nbsp;&nbsp; '+item[3]+'</option>');
				});

			}
		});

	}



})
