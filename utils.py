import hashlib
import requests
import xml.etree.ElementTree as ET
import simple_wechat_py.config as conf


def get_access_token():
    '''
    获取access_token
    '''
    if conf.ACCESS_TOKEN == '':
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            conf.APPID, conf.APPSECRET)
        resp, data = spider(url)
        conf.ACCESS_TOKEN = data['access_token']
        print('第一次获取access_token')
        return conf.ACCESS_TOKEN
    else:
        print('不需要再次获取%s' % conf.ACCESS_TOKEN)
        return conf.ACCESS_TOKEN


def check_signature(token, signature, timestamp, nonce):
    '''
    验证微信接口
    '''
    L = [timestamp, nonce, token]
    L.sort()
    str = '%s%s%s' % tuple(L)
    return hashlib.sha1(str.encode()).hexdigest() == signature


def parse_msg(body):
    '''
    解析XML
    '''
    root = ET.fromstring(body)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg


def spider(url, method='get', data=None, files=None):
    method = method.upper()
    if method == 'GET':
        r = requests.get(url)
    elif method == 'POST':
        r = requests.post(url, data=data, files=files)
    else:
        raise NameError('请求方法有误')
    if r.status_code is requests.codes.ok:
        response_headers = dict(r.headers)
        content_type = r.headers['content-type']
        if 'application/json' in content_type:
            print('返回json')
            return response_headers, r.json()
        elif 'text/plain' in content_type:
            print('返回文本')
            return response_headers, r.text
        else:
            print('返回二进制')
            return response_headers, r.content
