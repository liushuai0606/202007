# Come on! boy!

import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result_mac = re.match(r'(\d*)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)',
                      mac.strip()).groups()

result_format = '{0:<10}: {1:<30}'

print('-'*80)
print(result_format.format('VLAN ID', result_mac[0]))
print(result_format.format('MAC', result_mac[1]))
print(result_format.format('Type', result_mac[2]))
print(result_format.format('Interface', result_mac[3]))



mac2 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result_mac2 = re.match(r'(\w+)+ server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})+ localserver\s+'
                   r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),+ idle\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),'
                   r' bytes\s+(\d+),+ flags\s+(\w+)',mac2.strip()).groups()

result_format = '{0:<15}: {1:<30}'

print('-'*80)
print(result_format.format('protocol', result_mac2[0]))
print(result_format.format('server', result_mac2[1]))
print(result_format.format('localserver', result_mac2[2]))
print(result_format.format('idle', result_mac2[3]+' 小时 '+result_mac2[4]+' 分钟 '+result_mac2[5]+' 秒 '))
print(result_format.format('bytes', result_mac2[6]))
print(result_format.format('flags', result_mac2[7]))
