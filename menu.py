import json
from simple_wechat_py import utils


class Menu(object):
    def __init__(self):
        pass

    def create_menu(self, body):
        '''
        创建菜单
        :param body: json
        :return: 布尔值
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % utils.get_access_token()
        resp, data = utils.spider(url, method='post', data=json.dumps(body, ensure_ascii=False).encode('utf-8'))
        print(data)
        if data['errmsg'] == 'ok':
            return True
        else:
            return False

    def del_menu(self):
        '''
        删除菜单
        :return: 布尔值
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s' % utils.get_access_token()
        resp, data = utils.spider(url)
        if data['errmsg'] == 'ok':
            return True
        else:
            return False
