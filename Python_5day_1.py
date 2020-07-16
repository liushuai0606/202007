# Come on! boy!

import os
import re
gateway_result = os.popen('route -n').read()

for route in gateway_result.strip().split('\n')[2:]:
    re_route = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                        r'(\w+)\s+\d+\s+\d+\s+\d+\s+\w',route.strip()).groups()

    if re_route[1] == 'UG':
        print('网关为：' ,re_route[0])