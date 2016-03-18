import json
from simple_wechat_py import utils
import mimetypes
import time


class Media(object):
    def __init__(self):
        pass

    def create_media(self, type, path):
        '''
        上传临时素材
        :param type: 图片（image）、语音（voice）、视频（video）和缩略图（thumb）
        :param path: 本地素材路径
        :return: 素材ID
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s' % (
            utils.get_access_token(), type)
        with open(path, 'rb') as data:
            file = data.read()
            resp, content = utils.spider(url, method='post', files={'file': (path, file)})
            my_data = json.loads(content)
            return my_data['media_id']

    def get_media(self, m_id, path):
        '''
        获取临时素材
        :param m_id: 素材ID
        :param path: 素材存放目录
        :return: 素材的本地地址
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s' % (
            utils.get_access_token(), m_id)
        resp, content = utils.spider(url)
        new_path = '%s/%s%s' % (path, int(time.time()), mimetypes.guess_extension(resp['content-type']))
        with open(new_path, 'wb') as data:
            data.write(content)
            return new_path
