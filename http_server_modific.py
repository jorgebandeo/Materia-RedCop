import http.server
import os

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            files = os.listdir('.')
            file_list = '<ul>'
            for file in files:
                file_list += f'<li>{file}</li>'
            file_list += '</ul>'
            content = f"<html><body><h1>Arquivos no diretório raiz:</h1>{file_list}</body></html>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        else:
            self.send_error(404)
            
def run_server():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()