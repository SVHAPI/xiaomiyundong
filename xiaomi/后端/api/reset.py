import requests,time
tim = str(round(time.time() * 1000))

r = 'A29E05DA31065BC0ED6CEA7050808B6E50FD566F01000000E8CB9F0101000000'

def cap(phone):
    global r
    url = 'https://api-user-cn2.huami.com/registrations/+86{}/password?country_code=CN&r={}&t={}'.format(phone,r,tim)
    code = requests.delete(url).status_code
    # 获取验证码
    print(code)
    if code == 429:
        return '此账号发送验证码已达到极限'
    if code == 404:
        return '此账号未注册'

def rese(phone,password,code):
    global r
    url = 'https://api-user-cn2.huami.com/registrations/+86{}/findPassword/verify'.format(phone)
    data = {'code': code,'country_code':'CN','r':r,'t': tim}
    r = requests.post(url,data).json()
    if r['code'] != 4:
        reset = r['code']
    else:
        return '验证码错误'
    # 验证验证码是否正确
    url = 'https://api-user-cn2.huami.com/registrations/+86{}/password'.format(phone)
    data = {'country_code': 'CN','new': password,'r': r,'reset': reset,'t': tim}
    r = requests.post(url,data)
    return '修改成功'

def main(phone,password,code):
    # 重置密码
    print(phone,password,code)
    if code == None:
        return cap(phone)
    else:
        return rese(phone,password,code)
