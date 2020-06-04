
# 收集线程
import logging
import time
import requests

from queue import Empty
from .base import BaseThread


class Host(BaseThread):
    """收集主机硬件信息"""

    def __init__(self, queue):
        super().__init__(queue, 'host', 10)
        self.items = queue.ITEMS

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/'.format('192.168.31.100'),
            'msg' : {
                'name' : 'test1',
                'os' : 'ubuntu 16.04',
                'project' : self.items
            }

        }

