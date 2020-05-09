import time

from Bakup.Web.www.coroweb import get

from Bakup.Web.www.model import Device


@get('/')
def index(request):
    summary = 'test'
    summary_MikroTik = 'MikroTik RouterOS是一种路由操作系统，并通过该软件将标准的PC电脑变成专业路由器'
    devices = [
        Device(id='1', name='MikroTik Router', summary=summary_MikroTik, created_at=time.time() - 120),
        Device(id='2', name='TP-Link Router', summary=summary, created_at=time.time() - 3600),
        Device(id='3', name='TP-Link Router', summary=summary, created_at=time.time() - 3600),
    ]
    return {
        '__template__': 'devices.html',
        'blogs': devices
    }
