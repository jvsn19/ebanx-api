import http.server
import socketserver
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer

from utils import ConnectionHandler

def get_args() -> None:
    parser = ArgumentParser(description = 'Simple handmade API server. To start you need to pass some attributes')
    parser.add_argument('--address', dest = 'address', default='127.0.0.1', help = 'url that will receive requests.')
    parser.add_argument('--port', dest = 'port', default=8080, help = 'port that will receive requests')
    args = parser.parse_args()

    return args

def close_connection(server: socketserver.TCPServer) -> None:
    server.close_request()

def main() -> None:
    args = get_args()
    httpd = HTTPServer((args.address, args.port), ConnectionHandler)

    request = httpd.serve_forever()

if __name__ == '__main__':
    main()
