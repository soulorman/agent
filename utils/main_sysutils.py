#encoding: utf-8
import socket
import platform
import subprocess

def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_hostname():
    return socket.gethostname()

def get_arch():
    return platform.architecture()[0]

def get_os():
    return platform.linux_distribution()[0]+" "+platform.linux_distribution()[1]

def get_kernel():
    return platform.release()

def get_cpu_number():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l")

def get_cpu_core():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'core id' | sort | uniq | wc -l")

def get_cpu_vcore():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'processor' | sort | uniq | wc -l")

def get_disk_info():
    # 上传服务器字典乱序，但是改成其他类型，上传的时候符号不对  总是[]
    disk_name = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $1}'").split('\n')
    disk_size = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $4}'").split('\n')
    return dict(zip(disk_name,disk_size))

def get_mem_info():
    return subprocess.getoutput("dmidecode -t memory|grep 'Size'|awk '{print $2$3$4}'|grep -v 'No'").split('\n')

def get_gpu_info():
    result =  subprocess.getoutput("nvidia-smi -q|grep 'Product Name'|awk '{print $4\" \"$5\" \"$6}'").split('\n')
    if 'not found' in str(result):
        return '无显卡'
    else:
        return result
        
if __name__ == '__main__':
    print(get_addr())
    print(get_hostname())
    print(get_arch())
    print(get_os())
    print(get_kernel())
    print(get_cpu_number())
    print(get_cpu_core())
    print(get_cpu_vcore())
    print(get_disk_info())
    print(get_mem_info())
    print(get_gpu_info())
