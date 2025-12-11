import http.server
import socketserver

PORT = 8000
HANDLER = http.server.BaseHTTPRequestHandler

class RequestHandler(HANDLER):

    def do_GET(self):
        self.send_response(200)
        
        self.send_header = 'text/html'
        self.end_headers()

        message = "<h1>Hello from Python Web Server!</h1>"
        message += "<p>You requested the path: <strong>{}</strong></p>".format(self.path)

        self.wfile.write(bytes(message, 'utf-8'))

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # Keep the server running until interrupted (e.g., Ctrl+C)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopping...")
        httpd.server_close()