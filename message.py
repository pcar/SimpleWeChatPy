import time


class Message(object):
    def __init__(self):
        pass

    def send_text(self, content, msg):
        '''
        回复文本
        '''
        tpl = ''' <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                </xml>'''
        echo_str = tpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content)
        return echo_str

    def send_image(self, m_id, msg):
        '''
        回复图片
        '''
        tpl = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[image]]></MsgType>
                    <Image>
                        <MediaId><![CDATA[%s]]></MediaId>
                    </Image>
                </xml>'''
        echo_str = tpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), m_id)
        return echo_str

    def send_voice(self, m_id, msg):
        '''
       回复语音
       '''
        tpl = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[voice]]></MsgType>
                    <Voice>
                        <MediaId><![CDATA[%s]]></MediaId>
                    </Voice>
                </xml>'''
        echo_str = tpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), m_id)
        return echo_str

    def send_video(self, m_id, msg, title='', description=''):
        '''
        回复视频
        '''

        tpl = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[video]]></MsgType>
                    <Video>
                        <MediaId><![CDATA[%s]]></MediaId>
                        <Title><![CDATA[%s]]></Title>
                        <Description><![CDATA[%s]]></Description>
                    </Video>
                </xml>'''
        echo_str = tpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), m_id, title, description)
        return echo_str

    def send_music(self, music_url, msg, title='', description='', HQ_music_url='', thumb_m_id=''):
        '''
       回复音乐
       '''
        tpl = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[music]]></MsgType>
                    <Music>
                        <Title><![CDATA[%s]]></Title>
                        <Description><![CDATA[%s]]></Description>
                        <MusicUrl><![CDATA[%s]]></MusicUrl>
                        <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
                        <ThumbMediaId><![CDATA[%s]]></ThumbMediaId>
                    </Music>
                </xml>'''
        echo_str = tpl % (
            msg['FromUserName'], msg['ToUserName'], str(int(time.time())), title, description, music_url, HQ_music_url,
            thumb_m_id)
        return echo_str

    def send_news(self, list, msg):
        '''
        回复图文
        '''
        tpl = '''
        <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>%s</ArticleCount>
            <Articles>%s</Articles>
        </xml>  '''
        new_tpl = '''
        <item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
        </item>
        '''
        news = ''
        for data in iter(list[:10]):
            news += new_tpl % (data['title'], data['description'], data['pic'], data['url'])
        echo_str = tpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), len(list[:10]), news)
        return echo_str
