from simple_wechat_py import utils
import json
import math


class User(object):
    def __init__(self):
        pass

    def get_open_id_list(self, next_openid=None):
        '''
        获取1万个OpenID
        :param next_openid: 结束的ID
        :return: {"total":23000,"count":10000,"data":{"openid":["","OPENID1","OPENID2"]},"next_openid":"NEXT_OPENID"}
        '''
        next_openid = next_openid if next_openid else ''
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
            utils.get_access_token(), next_openid)
        resp, data = utils.spider(url)
        return data

    def batch_open_id_list(self, next_openid=None):
        '''
        获取全部OpenId
        :param next_openid:
        :return: [openid1,openid2]
        '''
        data = []
        init_data = self.get_open_id_list(next_openid)
        total = init_data['total']
        next_openid = init_data['next_openid']
        num = math.ceil(total / 10000) if total > 10000 else 0
        data.extend(init_data['data']['openid'])
        for i in range(0, num):
            json_data = self.get_open_id_list(next_openid)
            data.extend(json_data['data']['openid'])
            next_openid = json_data['next_openid']
        return data

    def get_user_info(self, o_id):
        '''
        获取用户信息
        :param o_id:
        :return:
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN' % (
            utils.get_access_token(), o_id)
        resp, data = utils.spider(url)
        return data

    def batch_user_info_list(self, data):
        '''
        获取100条用户信息
        :param data:
        [{
            "openid": "otvxTs4dckWG7imySrJd6jSi0CWE",
            "lang": "zh-CN"},
            {"openid": "otvxTs_JZ6SEiP0imdhpi50fuSZg",
            "lang": "zh-CN"
        }]
        :return:{ "user_info_list": [{},{}]}
        '''
        data = {"user_list": data}
        url = 'https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token=%s' % utils.get_access_token()
        resp, content = utils.spider(url, 'post', json.dumps(data))
        return content
