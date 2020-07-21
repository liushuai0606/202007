# Come on! boy!

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    # ping_result.show()
    if ping_result:
        return ip, True
    else:
        return ip, False


if __name__== '__main__':
    result = qytang_ping('192.168.1.1')
    if result[1]:
        print(f'{result[0]} 通！')
    else:
        print(f'{result[0]} 不通！')
