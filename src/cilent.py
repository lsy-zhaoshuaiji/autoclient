import requests,json
from lib.conf.config import settings
from src.plugins import pluginManager
from concurrent.futures import ThreadPoolExecutor
from lib.utils import PrpCrypt,auth

class Base():
    def port_asset(self,serverinfo):
        obj=PrpCrypt(settings.DATA_KEY)

        serverinfo = {'board': {'status': True, 'data': {'sn': '2102310TQE10DC000344'}}, 'cpu': {'status': True, 'data': {'cpu_model': ' Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz'}}, 'disk': {'status': True, 'data': {'total': '123G'}}, 'memory': {'status': True, 'data': {'total': '81G'}}, 'nic': {'status': True, 'data': {'enp1s0f0': {'up': True, 'hwaddr': '48:46:fb:f8:69:05', 'ipaddrs': '', 'netmask': ''}, 'enp1s0f1': {'up': True, 'hwaddr': '48:46:fb:f8:69:66', 'ipaddrs': '192.168.1.15', 'netmask': '255.255.255.0'}}}}

        data=obj.encrypt(json.dumps(serverinfo))
        try:
            requests.post(url=settings.API,
                      data=data,
                      headers={'OpenKey':auth(),'Content-Type':'application/json'},
                      )
            print('发送成功')
        except:
            print('发送信息失败')
class Agent(Base):
    def execute(self):
        serverinfo=pluginManager().exe_plugin()
        return self.port_asset(serverinfo)
class SSHSALT(Base):
    def get_host(self):
        response=requests.get(settings.API)
        ret=json.load(response.text)
        if not ret['status']:
            return
        return ret['data']
    def task(self,host):
        serverinfo = pluginManager(host).exe_plugin()
        self.port_asset(serverinfo)
    def execute(self):
        host_list=self.get_host()
        pool = ThreadPoolExecutor(10)          #通过线程池来提高效率
        for host in host_list:
            pool.submit(self.task,host)
            # serverinfo = pluginManager(host).exe_plugin()
            # return self.port_asset(serverinfo)


'''
cd ..
rm -rf uwsgi.log
pkill -9 -f uwsgi
uwsgi -x socket.xml
vim uwsgi.log
killall nginx
systemctl restart nginx
'''