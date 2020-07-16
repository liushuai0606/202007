# Come on! boy!

#!/usr/bin/python3.6
# -*- coding=utf-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 81
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
