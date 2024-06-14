#!/usr/bin/env python3
# A web server to serve a static HTML file and log POST request data.
#
# Usage: ./webserver
#        ./webserver 0.0.0.0:5000

from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
import os

BIND_HOST = "localhost"
PORT = 8008
HTML_FILE = "inktrap.html"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read and serve the HTML file
        try:
            with open(HTML_FILE, 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.wfile.write(b"<html><body><h1>File not found</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers.get("content-length", 0))
        body = self.rfile.read(content_length)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Received POST data")

        # Log the POST request headers and body to the console
        print(self.headers)
        print(body.decode("utf-8"))

if len(argv) > 1:
    arg = argv[1].split(":")
    BIND_HOST = arg[0]
    PORT = int(arg[1])

print(f"Listening on http://{BIND_HOST}:{PORT}\n")

httpd = HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
