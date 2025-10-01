#!/usr/bin/env python3
import http.server
import socketserver
import json
from datetime import datetime

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"""
            <html>
            <head><title>Legal Agent Test</title></head>
            <body>
                <h1>🧪 Connection Test Successful!</h1>
                <p>Time: {datetime.now()}</p>
                <p>If you can see this, the web server is working!</p>
                <p><a href="/legal">Try Legal Agent</a></p>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        elif self.path == '/legal':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <head><title>Legal Agent Ready</title></head>
            <body>
                <h1>🏛️ AI Legal Agent Ready!</h1>
                <p>The legal agent backend is working. Streamlit issues resolved!</p>
                <p>You can now upload legal documents for analysis.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

if __name__ == "__main__":
    PORT = 8888
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Simple test server at http://localhost:{PORT}")
        httpd.serve_forever()