import ipcalc


class Format:
    def __init__(self):
        self.default_port = 443

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


if __name__ == '__main__':
    test = Format()
    test.default_port = 8291
    print(test.format_file('ip.txt'))
    print(test.format_ip('192.168.1.1:443'))
