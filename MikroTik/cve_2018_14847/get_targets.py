def format_single_ip(target):
    target_info = []
    target_info_list = target.split(':')
    if len(target_info_list) == 1:
        ip = [target_info_list[0], 8291]
        target_info.append(ip)
    elif len(target_info_list) == 2:
        ip = [target_info_list[0], int(target_info_list[1])]
        target_info.append(ip)
    return target_info


def format_file(filename):
    target_info = []
    for line in open(filename, 'r'):
        target_info_list = line.strip().split(':')
        if len(target_info_list) == 1:
            ip = [target_info_list[0], 8291]
            target_info.append(ip)
        elif len(target_info_list) == 2:
            ip = [target_info_list[0], int(target_info_list[1])]
            target_info.append(ip)
    return target_info


if __name__ == '__main__':
    print(format_file('result.txt'))
    print(format_single_ip('192.168.161.222:2222'))
    print(format_single_ip('192.168.11.11'))
