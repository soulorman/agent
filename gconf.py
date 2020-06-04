#gconf.py
# encoding: utf-8
from queue import Queue

class Config(object):
    '''设置并传递配置和队列'''

    def __init__(self, args):
        self.SERVER = '{0}:{1}'.format(args.host, args.port)
        self.ITEMS = args.items
        self.QUEUE = Queue()
