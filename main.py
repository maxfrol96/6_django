from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        data = "Hello, World wide web!"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))


webServer = HTTPServer((host, port), MyServer)

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
