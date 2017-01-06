$(function(){


	var error_name = false;
	var error_password = false;


	$('#username').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});



	function check_user_name(){
		var value1 = $('#username').val();
		var len=$('#username').val().length;
		if(len<5||len>20)
		{
			$('#username').next().html('请输入5-20个字符的用户名')
			$('#username').next().show();
			error_name = true;
		}
		else
		{
			$.get('/usermode/register_checkname/',{uname:value1},function(data){
				if(data.isOnly=='yes'){
					$('#username').next().html('用户名不存在!')
					$('#username').next().show();
					error_name = true;
				}else{
					$('#username').next().hide();
					error_name = false;
				}
			})
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}




	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();

		if(error_name == false && error_password == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});


	//记住用户名
	//写cookies
	function setCookie(c_name, value, expiredays){
	 　　　　var exdate=new Date();
	　　　　exdate.setDate(exdate.getDate() + expiredays);
	　　　　document.cookie=c_name+ "=" + escape(value) + ((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
	 　　}

	//读取cookies
	function getCookie(name)
	{
	 var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");

	 if(arr=document.cookie.match(reg))

	  return (arr[2]);
	 else
	  return null;
	}

	//删除cookies
	function delCookie(name)
	{
	 var exp = new Date();
	 exp.setTime(exp.getTime() - 1000);
	 var cval=getCookie(name);
	 if(cval!=null)
	  document.cookie= name + "="+cval+";expires="+exp.toGMTString();
	}


	$('.more_input input').click(function(){
		var ischecked=$(this).prop("checked")
		if(ischecked=true){
			var frename=$('#username').val()
			setCookie('frename',frename,7)
			alert(getCookie("frename"));
		}else{
			delCookie("frename")
			alert(getCookie("frename"));
		}
	})






})