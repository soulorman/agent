
# encoding: utf-8
import logging
from threading import Thread
import time

logger = logging.getLogger(__name__)

class BaseThread(Thread):
    '''基础线程'''

    def __init__(self, config, type, interval):
        super().__init__()
        self.daemon = True
        self._config = config
        self._type = type
        self._interval = interval

    def make_event(self):
        return None

    def run(self):
        '''写进队列，或者发送队列'''
        _config = self._config
        _type = self._type
        _interval = self._interval

        _queue = _config.QUEUE
        logger.info('plugin[ %s ] running ...', _type)
        
        while True:
            evt = self.make_event()
            if evt:
                logger.debug('plugin[ %s ] make event: %s', _type, evt.get('msg',None))
                _queue.put(evt)

            time.sleep(_interval)



