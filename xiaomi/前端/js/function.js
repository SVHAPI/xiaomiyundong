function ttl() {
    let phone = document.querySelector("#phone").value
	if (phone == "") {
		alert('手机号不能为空！')
		return
	}
	let pass = document.querySelector("#pwd").value
	if (pass == "") {
		alert('密码不能为空！')
		return
	}
	let count = document.querySelector("#step").value
	if (count == "") {
		alert('步数不能为空！')
		return
	}
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var myArr = JSON.parse(this.responseText);
            console.log(myArr);
            if (myArr.code == 1){
                alert('步数提交成功')
            }else{
                alert('账号或密码不正确')
            }
        }
    }
    xhttp.open("POST", "https://vhapi.com/ttl", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone + '&password=' + pass + '&ttl=' + count
    xhttp.send(data);
}

let code = true
function getcode() {
    let phone = document.querySelector("#phone").value
    if (phone == "") {
        alert('手机号不能为空！')
        return
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function()
    {
        if (xhttp.readyState==4 && xhttp.status==200)
        {
            var myArr = JSON.parse(this.responseText);
            console.log(myArr.msg);
            if (myArr.msg == '此账号已注册'){
                alert('账号已被注册过了无法再次注册！')
            }else if (myArr.msg == '此账号发送验证码已达到极限'){
                alert('此账号发送验证码已达到极限')
            }else if (myArr.msg == '账号或密码格式不对'){
                alert('账号或密码格式不对')
            }else{
                alert('验证码发送成功')
                code = false
            }
        }
    }
    xhttp.open("POST", "https://vhapi.com/captcha", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone
    xhttp.send(data);
}

function register() {
    let phone = document.querySelector("#phone").value
    if (phone == "") {
        alert('手机号不能为空！')
        return
    }
    let pass = document.querySelector("#pwd").value
    if (pass == "") {
        alert('密码不能为空！')
        return
    }
    let count = document.querySelector("#step").value
    if (count == "") {
        alert('验证码不能为空！')
        return
    }
    if (code){
        alert('请先获取验证码！')
        return
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function()
    {
        if (xhttp.readyState==4 && xhttp.status==200)
        {
            var myArr = JSON.parse(this.responseText);
            alert(myArr.msg)
            if (myArr.msg == '注册成功'){
                var config ={
                    width:200,
                    height:200,
                    text:myArr.url,
                    render : "canvas",
                    background:"#FFFFFF",
                    foreground:"#000000",
                };
                $("#img").qrcode(config);
            }
        }
    }
    xhttp.open("POST", "https://vhapi.com/register", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone + '&password=' + pass + '&code=' + count
    xhttp.send(data);
}

let rcode = true
function reset() {
	let phone = document.querySelector("#phone").value
	if (phone == "") {
		alert('手机号不能为空！')
		return
	}
	let pass = document.querySelector("#pwd").value
	if (pass == "") {
		alert('密码不能为空！')
		return
	}
	let count = document.querySelector("#step").value
	if (count == "") {
		alert('验证码不能为空！')
		return
	}
    if (rcode){
        alert('请先获取验证码！')
		return
    }
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function()
    {
        if (xhttp.readyState==4 && xhttp.status==200)
        {
            var myArr = JSON.parse(this.responseText);
            alert(myArr.msg)
        }
    }
    xhttp.open("POST", "https://vhapi.com/reset", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone + '&password=' + pass + '&code=' + count
    xhttp.send(data);
}

function getrcode() {
    let phone = document.querySelector("#phone").value
	if (phone == "") {
		alert('手机号不能为空！')
		return
	}
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function()
    {
        if (xhttp.readyState==4 && xhttp.status==200)
        {
            var myArr = JSON.parse(this.responseText);
            console.log(myArr.msg);
            if (myArr.msg == '此账号发送验证码已达到极限'){
                alert('此账号发送验证码已达到极限')
            }else{
                alert('验证码发送成功')
                rcode = false
            }
        }
    }
    xhttp.open("POST", "https://vhapi.com/reset", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone
    xhttp.send(data);
}

function creatwxqr() {
    let phone = document.querySelector("#phone").value
    if (phone == "") {
        alert('手机号不能为空！')
        return
    }
    let pass = document.querySelector("#pwd").value
    if (pass == "") {
        alert('密码不能为空！')
        return
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function()
    {
        if (xhttp.readyState==4 && xhttp.status==200)
        {
            var myArr = JSON.parse(this.responseText);
            $("#img").html("");
            if (myArr.url != undefined){
                var config ={
                    width:200,
                    height:200,
                    text:myArr.url,
                    render : "canvas",
                    background:"#FFFFFF",
                    foreground:"#000000",
                };
                $("#img").qrcode(config);
            }else{
                alert('账号或密码错误')
            }
        }
    }
    xhttp.open("POST", "https://vhapi.com/createwxqr", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var data = 'phone=' + phone + '&password=' + pass
    xhttp.send(data);
}