import requests
def main(app_token,thirdPartyId,userid):
    # 获取绑定微信二维码
    deviceid = 'mifit_{}_huami_{}_thirdpartyId'.format(userid,thirdPartyId)
    url = 'https://api-mifit-cn2.huami.com/huami.health.createwxqr.json?deviceid={}&thirdPartyId={}&userid={}'.format(deviceid,thirdPartyId,userid)
    data = {'app_token':app_token}
    wxqr = requests.get(url,data).json()
    return wxqr['data']['list']