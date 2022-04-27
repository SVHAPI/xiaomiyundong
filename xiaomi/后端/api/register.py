import requests,time
from . import login
tim = str(round(time.time() * 1000))
def main(code,phone,password):
    # 小米运动注册
    print(code,phone,password)
    r = 'A29E05DA31065BC0ED6CEA7050808B6E90453D6B01000000E88BB90501000000'
    url = 'https://api-user.huami.com/registrations/+86{}'.format(phone)
    headers = {
        'Host': 'api-user.huami.com',
        'Accept': '*/*',
        'app_name': 'com.xiaomi.hm.health',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate, br',
        'callid': tim,
        'Content-Length': '281',
        'shouldHookRedirection': 'YES',
        'X-Request-Id': '1D0FDAD2-A2CB-47A8-A529-5885407D32F4',
        'cv': '6.0.3',
        'lang': 'zh_CN',
        'timezone': 'Asia/Shanghai',
        'appplatform': 'ios_phone',
        'country': 'CN',
        'User-Agent': 'ZeppLife/6.0.3 (iPhone; iOS 15.3; Scale/3.00)',
        'Connection': 'keep-alive'
    }
    data = {
        'client_id': 'HuaMi',
        'code': code,
        'country_code': 'CN',
        'name': '',
        'password': password,
        'r': r,
        'redirect_uri': 'https%3A//s3-us-west-2.amazonaws.com/hm-registration/successsignin.html',
        'state': 'REDIRECTION',
        't': tim,
        'token':'access',
        'token':'refresh',
    }
    code = requests.post(url=url, headers=headers, data=data, allow_redirects=False)
    # 注册用户
    access = login.main(phone,password)
    url = 'https://account.huami.com/v1/client/register' 
    headers = {
        'Host': 'account.huami.com',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate, br',
        'callid': tim,
        'X-Request-Id': 'B4FBE62B-E666-4D69-8C6F-BD3D133FBA0F',
        'Content-Length': '562',
        'cv': '6.0.3',
        'lang': 'zh_CN',
        'timezone': 'Asia/Shanghai',
        'appplatform': 'ios_phone',
        'country': 'CN',
        'User-Agent': 'ZeppLife/6.0.3 (iPhone; iOS 15.3; Scale/3.00)',
        'Connection': 'keep-alive'
    }
    data = {
        'app_name': 'com.xiaomi.hm.health',
        'app_version': '6.0.3',
        'code': access,
        'country_code': 'CN',
        'device_id': 'E5FC24A9-F200-4BD1-9CF7-A411D06FD715',
        'device_id_type': 'uuid',
        'device_model': 'phone',
        'dn': 'api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com%2Caccount.huami.com%2Capi-watch.huami.com%2Cauth.huami.com',
        'grant_type': 'access_token',
        'lang': 'zh_CN',
        'os_version': '1.5.0',
        'source': 'com.xiaomi.hm.health',
        'third_name': 'huami_phone',
    }
    requests.post(url, headers=headers, data=data).json()