import psutil
import platform
import cpuinfo
import sysconfig


class SystemInfo:
    def __init__(self):
        self.data = {}
        self.info = cpuinfo.get_cpu_info()

    def get_cpu_info(self):
        cpu_info = {}

        cpu_info['Cpu Model'] = self.get_cpu_model()
        cpu_info['Cpu Count'] = self.get_cpu_count()
        cpu_info['Cpu Core Count'] = self.get_cpu_core_count()
        cpu_info['Cpu Vendor'] = self.get_cpu_vendor()
        cpu_info['Cpu Speed'] = self.get_cpu_speed()
        return cpu_info

    def get_ram_info(self):
        ram_info = {}
        ram_info['Ram Total'] = f'{self.get_ram_total() / 1024 / 1024 / 1024:.2f} GB'
        ram_info['Ram Used'] = f'{self.get_ram_used() / 1024 / 1024 / 1024:.2f} GB'
        ram_info['Ram Free'] = f'{self.get_ram_free() / 1024 / 1024 / 1024:.2f} GB'
        ram_info['Ram Percent'] = f'{self.get_ram_percent()} %'
        return ram_info

    def get_disk_info(self):
        disk_info = {}
        disks = psutil.disk_partitions()
        total = 0
        for disk in disks:
            disk_info[disk.device] = {}
            disk_info[disk.device]['Fstype'] = disk.fstype
            disk_info[disk.device]['Opts'] = disk.opts
            disk_info[disk.device]['Total'] = f'{self.get_disk_total(disk.mountpoint) / 1024 / 1024 / 1024:.2f} GB'
            disk_info[disk.device]['Disk Used'] = f'{self.get_disk_used(disk.mountpoint) / 1024 / 1024 / 1024:.2f} GB'
            disk_info[disk.device]['Disk Free'] = f'{self.get_disk_free(disk.mountpoint) / 1024 / 1024 / 1024:.2f} GB'
            disk_info[disk.device]['Disk Percent'] = f'{self.get_disk_percent(disk.mountpoint)} %'
            total += self.get_disk_total(disk.mountpoint)

        disk_info['Total'] = f'{total / 1024 / 1024 / 1024:.2f} GB'
        return disk_info

    def get_os_info(self):
        os_info = {}
        os_info['Os Type'] = self.get_os_name()
        os_info['Os Platform'] = self.get_os_platform()
        os_info['Os Version'] = self.get_os_version()
        os_info['Os Release'] = self.get_os_release()
        os_info['Os Type'] = self.get_os_type()
        return os_info

    @staticmethod
    def get_hostname():
        return platform.node()

    def get_cpu_model(self):
        return self.info['brand_raw']

    @staticmethod
    def get_cpu_count():
        return psutil.cpu_count(logical=False)

    def get_cpu_core_count(self):
        return self.info['count']

    def get_cpu_vendor(self):
        return self.info['vendor_id_raw']

    def get_cpu_speed(self):
        return self.info['hz_actual_friendly']

    @staticmethod
    def get_ram_total():
        return psutil.virtual_memory().total

    @staticmethod
    def get_ram_used():
        return psutil.virtual_memory().used

    @staticmethod
    def get_ram_free():
        return psutil.virtual_memory().free

    @staticmethod
    def get_ram_percent():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_disk_total(mountpoint):
        return psutil.disk_usage(mountpoint).total

    @staticmethod
    def get_disk_used(mountpoint):
        return psutil.disk_usage(mountpoint).used

    @staticmethod
    def get_disk_free(mountpoint):
        return psutil.disk_usage(mountpoint).free

    @staticmethod
    def get_disk_percent(mountpoint):
        return psutil.disk_usage(mountpoint).percent

    @staticmethod
    def get_os_platform():
        return sysconfig.get_platform()

    @staticmethod
    def get_os_version():
        return platform.uname().version

    @staticmethod
    def get_os_release():
        return platform.uname().release

    @staticmethod
    def get_os_type():
        return platform.uname().system

    @staticmethod
    def get_os_name():
        return sysconfig.get_platform()

