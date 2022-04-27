import requests,re
def main(user,password):
    # 登录
    url = "https://api-user.huami.com/registrations/+86" + user + "/tokens"
    biao = {
        "client_id": "HuaMi",
        "password": password,
        "redirect_uri": "https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token": "access",
    }
    fc = requests.post(url=url, data=biao, allow_redirects=False)
    fx = fc.headers["Location"]
    access = re.findall('&access=(.*?)&',fx)
    if access:   
        print(user + "登陆成功")
        return access[0]
    else:
        print("账号或密码错误")
        return False