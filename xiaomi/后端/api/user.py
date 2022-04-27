import requests
def main(access):
    # 登录信息
    url = 'https://account.huami.com/v2/client/login'
    biao = {
        "allow_registration": "false",
        "app_name": "com.xiaomi.hm.health",
        "app_version": "4.10.0",  # 小运动版本
        "code": access,  # 登录返回code
        "country_code": "CN",
        "device_id": "73681DC0-3B18-4252",
        "device_id_type": "uuid",
        "device_model": "phone",
        "grant_type": "access_token",
        "lang": "zh_CN",
        "os_version": "1.5.0",
        "source": "com.xiaomi.hm.health",
        "third_name": "huami_phone",
    }
    f = requests.post(url,data=biao).json()
    info = f['token_info']
    app_token = info['app_token']
    user_id = info['user_id']
    thirdparty_info = f['thirdparty_info']
    third_id = thirdparty_info['third_id']
    data = {'app_token': app_token,'user_id': user_id,'thirdparty_info': thirdparty_info,'third_id': third_id}
    return data