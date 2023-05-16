#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

port = 8000
httpd = HTTPServer(('', port), RequestHandler)
print(f'Servidor rodando na porta {port}')
httpd.serve_forever()
