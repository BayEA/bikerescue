import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


def get_file(request):
    # note that this potentially makes every file on your computer readable by the internet
    print(request.path)
    directory = "/home/ubuntu/bikerescue/www"
    # try keep requested limited to directory
    path = request.path.split("?")[0]
    if path == '/':
        path = '/index.html'


    f = open(directory + path, "rb") 
    request.send_response(200)
    request.send_header(
                'Content-type',  mimetypes.guess_type(directory + path)[0])

    request.end_headers()
    request.wfile.write(f.read())
    f.close()

    return request.wfile.write('debug response condition')

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        return get_file(self)


httpd = HTTPServer(("0.0.0.0", 80), SimpleHTTPRequestHandler)
httpd.serve_forever()
