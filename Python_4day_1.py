# Come on! boy!

import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()

#正则表达式查找IP，掩码，广播和Mac地址
ipv4_add = re.findall(r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
mac_addr = re.findall(r'ether\s+([0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2})',
                      ifconfig_result)[0]


#格式化字符串
format_string = '{0:<15}: {1:<30}'

#打印结果
print(format_string.format('ipv4_add',ipv4_add))
print(format_string.format('netmask',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr))

#产生网关的IP地址
ipv4_list = ipv4_add.split('.')
ipv4_list[3] = '1'
gateway = '.'.join(ipv4_list)

#ping网关

ping_resul  = os.popen('ping '+ gateway + ' -c 1').read()

re_ping = re.findall(r'1 received', ping_resul)

print('\n我们假设网关IP地址为最后一位为1，因此网关IP地址为：192.168.1.1\n')

if re_ping:
    print('网关可达！')
else:
    print('网关不可达！')
