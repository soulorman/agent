import logging
import time
import requests

from queue import Empty
from threading import Thread
import hmac
import urllib
import urllib.parse

logger = logging.getLogger(__name__)

class ENS(Thread):
    '''发送消息到服务端'''

    def __init__(self, config):
        super().__init__()
        self._config = config

    def run(self):
        '''写进队列，或者发送队列'''

        _queue = self._config.QUEUE
        _handle = self.handle

        logger.info('plugin[ %s ] running ...', 'send')

        while True:
            try:
                evt = _queue.get(block=True, timeout=3)
                logger.debug('send get event: %s', evt)
                _handle(evt)
            except Empty:
                time.sleep(3)

    def handle(self, evt):
        '''发送事件'''
        key = '123456789'
        secret = 'abcdef'
        unix_time = int(time.time())
        sign = self.get_sign(evt.get('msg'), unix_time, key, secret)

        _url = 'http://{0}/api/v2/{1}'.format(self._config.SERVER, evt.get('url'))
        _url += '?' + urllib.parse.urlencode({'time' : unix_time, 'key' : key, 'sign' : sign})
        response = requests.post(_url, json=evt.get('msg'))
        if not response.ok:
            logger.error(response.text)
        else:
            logger.debug('handle evt[%s], result: %s',evt,response.text)


    def get_sign(self, data, time, key, secret):
        sign_data = data.copy()
        sign_data['time'] = time
        
        # 排序，不然会乱
        sorted_sign_data = sorted(sign_data.items())
        text_sign_data =  secret + ':' + urllib.parse.urlencode(sorted_sign_data)
        
        _hmac = hmac.HMAC(key.encode())
        _hmac.update(text_sign_data.encode())

        return _hmac.hexdigest()
