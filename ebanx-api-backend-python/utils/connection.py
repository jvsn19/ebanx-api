from http.server import BaseHTTPRequestHandler

class ConnectionHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(f"GET request for {self.path}".encode('utf-8'))

    # def do_POST(self):
