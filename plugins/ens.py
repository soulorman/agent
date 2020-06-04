import logging
import time
import requests

from queue import Empty
from threading import Thread

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
        pass
        #_url = 'http://{0}/api/{1}'.format(self._config.SERVER, evt.get('url'))
        #response = requests.post(_url, json=evt.get('msg'))
        #if not response.ok:
        #    logger.error(response.text)

        #else:
        #    logger.debug('handle evt[%s], result: %s',evt,response.text)
