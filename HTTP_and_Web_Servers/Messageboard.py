#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


memory = []

class MessageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        form_string = ''.join(['<html>',
                               '<body>',
                               '<title>Message Board</title>',
                               '<form method="POST" action="/">',
                               '  <textarea name="message"></textarea>',
                               '  <br>',
                               '  <button type="submit">Post it!</button>',
                               '</form>',
                               '<pre>',
                               '{}',
                               '</pre>',
                               '</body>',
                               '</html>'])
        memory_string = '\n'.join(memory)
        self.wfile.write(form_string.format(memory_string).encode())
            

    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        data = self.rfile.read(length).decode()
        message = parse_qs(data)['message'][0]
        message = message.replace("<", "&lt;")

        memory.append(message)
        self.send_response(303)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Location', '/')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
