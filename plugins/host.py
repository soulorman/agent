
from .base import BaseThread
from utils import main_sysutils


class Host(BaseThread):
    """收集主机硬件信息"""

    def __init__(self, queue):
        super().__init__(queue, 'host', 10)
        self.items = queue.ITEMS

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/'.format(main_sysutils.get_addr()),
            'msg' : {
                'name' : main_sysutils.get_hostname(),
                'os' : main_sysutils.get_os(),
                'kernel' : main_sysutils.get_kernel(),
                'arch' : main_sysutils.get_arch(),
                'cpu_number' : main_sysutils.get_cpu_number(),
                'cpu_core' : main_sysutils.get_cpu_core(),
                'cpu_vcore' : main_sysutils.get_cpu_vcore(),
                'get_mem_info' : main_sysutils.get_mem_info(),
                'disk_info' : main_sysutils.get_disk_info(),
                'get_gpu_info' : main_sysutils.get_gpu_info(),

                'project' : self.items,
                }
        }

