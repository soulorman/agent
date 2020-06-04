# encoding: utf-8
import argparse
import logging
import os

from gconf import Config
from plugins.ens import ENS
from plugins.host import Host

def action_options():
    '''执行选项功能'''

    parser = argparse.ArgumentParser(description='这是资产管理系统的客户端模块')
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Server Addr')
    parser.add_argument('-P', '--port', type=int, default=8000, help='Server Port')
    parser.add_argument('-I', '--items', type=str, default='ESD', help='Project Name')
    parser.add_argument('-v', '--version', action='version',version='V0.1')
    parser.add_argument('-V', '--verbose', action='store_true', help='DEBUG INFO')

    args = parser.parse_args()
    return args

def working_with_logs(args):
    '''处理日志模块'''
    logger = logging.getLogger('agent')
    level = logging.DEBUG if args.verbose else logging.INFO
    fmt= '[%(asctime)s] [%(levelname)s] %(message)s'
    base_dir = os.path.dirname(os.path.abspath(__file__))

    logging.basicConfig(
                        level =  level, 
                        format =  fmt, 
                        filemode = 'w',
                        filename= os.path.join(base_dir, 'logs', 'agentd.log'),
                    )
    pid = os.getpid()
    logger.info('agent started: [%s]', pid)
    
def main(config):
    '''启动多线程

    :param: config: 服务器地址和端口
    :return
    '''
    ths = []
    ths.append(ENS(config))
    ths.append(Host(config))

    for th in ths:
        th.start()

if __name__ == '__main__':
    args = action_options()
    working_with_logs(args)

    config = Config(args)
    main(config)
