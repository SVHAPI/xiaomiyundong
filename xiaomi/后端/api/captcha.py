import requests,time
tim = str(round(time.time() * 1000))
def main(phone):
    r = 'A29E05DA31065BC0ED6CEA7050808B6E90453D6B01000000E88BB90501000000'
    url = 'https://api-user.huami.com/registrations/+86{}?country_code=CN&r={}&t={}'.format(phone,r,tim)
    headers = {
        'Host': 'api-user.huami.com',
        'Accept': '*/*',
        'app_name': 'com.xiaomi.hm.health',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate, br',
        'callid': tim,
        'X-Request-Id': '1D0FDAD2-A2CB-47A8-A529-5885407D32F4',
        'cv': '6.0.3',
        'lang': 'zh_CN',
        'timezone': 'Asia/Shanghai',
        'appplatform': 'ios_phone',
        'country': 'CN',
        'User-Agent': 'ZeppLife/6.0.3 (iPhone; iOS 15.3; Scale/3.00)',
        'Connection': 'keep-alive'
    }
    code = requests.get(url,headers).status_code
    # code值为404则用户未注册验证码发送成功
    if code == 429:
        print('此账号发送验证码已达到极限')
        return '此账号发送验证码已达到极限'
    elif code == 200:
        print('此账号已注册')
        return '此账号已注册'
    # elif code == 404:
    #     return '账号或密码格式不对'
    return '发送成功'