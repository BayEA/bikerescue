import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


def parse_request(request):

    print(request.path)
    directory = "/home/ubuntu/bikerescue/www"

    # remove query params from request.path
    path = request.path.split("?")[0]
    
    if path == '/':
        # default file to load
        path = '/index.html'

    f = open(directory + path, "rb") 
    request.send_response(200)
    request.send_header('Content-type',
                        mimetypes.guess_type(directory + path)[0])

    request.end_headers()
    request.wfile.write(f.read())
    f.close()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        return parse_request(self)



httpds = HTTPServer(("0.0.0.0", 443), SimpleHTTPRequestHandler)
httpds.socket = ssl.wrap_socket(
    httpds.socket,
    keyfile="/etc/letsencrypt/live/bayareabikerescue.com/privkey.pem",
    certfile="/etc/letsencrypt/live/bayareabikerescue.com/fullchain.pem",
    server_side=True)
httpds.serve_forever()
