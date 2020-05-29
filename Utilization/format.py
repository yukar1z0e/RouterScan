import ipcalc


class Format:
    def __init__(self):
        self.target_list = []
        self.result = []
        self.port = 443

        # Old Version of Param Never Use(Only For CVE_2018_13379)
        self.default_port = 443

    # Old Version of Function Never Use(Only For CVE_2018_13379)
    def format_file(self, filename):
        target_info = []
        for line in open(filename, 'r'):
            target_check_list = line.strip().split('/')
            if len(target_check_list) == 1:
                target_info_list = line.strip().split(':')
                if len(target_info_list) == 1:
                    ip = [target_info_list[0], self.default_port]
                    target_info.append(ip)
                elif len(target_info_list) == 2:
                    ip = [target_info_list[0], int(target_info_list[1])]
                    target_info.append(ip)
            else:
                item = ipcalc.Network(line.strip())
                for i in item:
                    ip = [str(i), self.default_port]
                    target_info.append(ip)
        return target_info

    # Old Version of Function Never Use(Only For CVE_2018_13379)
    def format_ip(self, target):
        target_info = []
        target_check_list = target.split('/')
        if len(target_check_list) == 1:
            target_info_list = target.split(':')
            if len(target_info_list) == 1:
                ip = [target_info_list[0], self.default_port]
                target_info.append(ip)
            elif len(target_info_list) == 2:
                ip = [target_info_list[0], int(target_info_list[1])]
                target_info.append(ip)
        else:
            item = ipcalc.Network(target)
            for i in item:
                ip = [str(i), self.default_port]
                target_info.append(ip)
        return target_info

    # New Version Function
    def ImportFile(self, filename):
        with open(filename) as file:
            self.target_list = file.read().splitlines()

    # New Version Function
    def ImportSingle(self, ip):
        if not self.target_list:
            self.target_list.append(ip)

    # New Version Function
    def FormatValue(self, target):
        ret = []
        # 192.168.1.1 192.168.1.1:80 192.168.1.1/16
        if len(target.split(':')) == 2:
            # 192.168.1.1:80
            ip = target.split(':')[0]
            port = target.split(':')[1]
            ret.append([ip, port])
        elif len(target.split('/')) == 2:
            # 192.168.1.1/16
            ip_list = ipcalc.Network(target)
            for ip in ip_list:
                ret.append([str(ip), self.port])
        else:
            # 192.168.1.1
            ret.append([target, self.port])
        return ret

    # New Version Function
    def GetValue(self):
        self.result = []
        for target in self.target_list:
            self.result.extend(self.FormatValue(target))
        ret = self.result
        return ret

    # New Version Function
    def __del__(self):
        # print('del class')
        self.target_list = []
        self.result = []
        self.port = 443


if __name__ == '__main__':
    test = Format()
    test.default_port = 8291
    print(test.format_file('ip.txt'))
    print(test.format_ip('192.168.1.1:443'))
