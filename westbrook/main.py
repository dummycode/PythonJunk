from getStats import getStats
from isAveragingTripleDouble import isAveragingTripleDouble
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # A simple "Is he?"
        content = str((isAveragingTripleDouble(), getStats()))

        # Write content as utf-8 data
        self.wfile.write(bytes(content, "utf8"))
        return

# Server settings
# Choose port 8080, for port 80, which is normally used for a http server, you need root access
server_address = ('127.0.0.1', 8081)
httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
httpd.serve_forever()
