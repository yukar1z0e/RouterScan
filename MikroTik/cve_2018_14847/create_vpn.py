import paramiko


class SSHClient:

    def __init__(self):
        self.ssh = paramiko.SSHClient()

    def login(self, host, port, username, password):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, username, password, timeout=10)

    def execute(self, command):
        global stderr
        try:
            # print('command', command)
            stdin, stdout, stderr = self.ssh.exec_command(command)
            # print('stdin', stdin)
        except:
            print('stderr', stderr.read().decode('ascii'))
            return 'error'
        out = stdout.read()

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
        # print('bridge out\n',bri_out)
        bri_list = bri_out.split(b'\r\n\r\n')
        for i in range(0, len(bri_list) - 1):
            per_bri_list = bri_list[i].decode('ascii').split('mac-address=')
            # print(per_bri_list)

            per_mac_list = per_bri_list[1].split(' ')
            bri_mac_addr = per_mac_list[0]
            bri_mac_addr_list.append(bri_mac_addr)

            per_name_list = per_bri_list[0].split('name="')
            name_list = per_name_list[1].split('"')
            bri_name_list.append(name_list[0])

            # print(per_mac[0])
            # print(per_bri)
        # print('bridge info\n',bri_info)
        # print('bridge mac address list', bri_mac_addr_list, 'bridge name list', bri_name_list)
        return bri_mac_addr_list, bri_name_list

    # choose usable ethernet list
    def get_lan_ethernet(self):
        index_list = []
        lan_ethernet_list = []
        eth_info_list = self.get_ethernet()
        bri_mac_addr_list, bri_name_list = self.get_bridge()
        for i in range(0, len(eth_info_list)):
            for addr in bri_mac_addr_list:
                # for addr in bri_mac_addr_list:
                #     for i in range(0, len(eth_info_list)):
                if addr not in eth_info_list[i]:
                    index_list.append(i)
                else:
                    break
        # print(index_list)
        for index in set(index_list):
            if ('RS' in eth_info_list[index]) or ('R' in eth_info_list[index]):
                # print(eth_info_list[index])
                lan_ethernet_list.append(eth_info_list[index])
        # print('Lan List\n', lan_ethernet_list)
        return lan_ethernet_list

    # create vpn
    def create_vpn(self):
        lan_int = self.get_lan_ethernet()[0][2]
        bri_mac_addr_list, bri_name_list = self.get_bridge()

        self.ssh.execute('/ip address add address=192.168.100.121/24 interface=' + lan_int)

        self.ssh.execute('/ip pool add name="pptp-vpn-pool" ranges=192.168.100.10-192.168.100.30')
        self.ssh.execute(
            '/ppp profile add name="pptp-vpn-profile" use-encryption=yes local-address=192.168.100.121 dns-server=8.8.8.8,0.0.0.0 remote-address=pptp-vpn-pool')
        self.ssh.execute('/ppp secret add name=asdftest profile=pptp-vpn-profile password=test123!@# service=pptp')
        self.ssh.execute(
            '/interface pptp-server server set enabled=yes default-profile=pptp-vpn-profile authentication=mschap2,mschap1,chap,pap')
        self.ssh.execute(
            '/ip firewall nat add chain=srcnat src-address=192.168.100.121/24 out-interface=' + bri_name_list[
                0] + ' action=masquerade')

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
    vpn.create_vpn()
    vpn.disconnect()