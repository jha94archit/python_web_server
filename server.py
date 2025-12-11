import http.server
import socketserver

PORT = 8000
HANDLER = http.server.BaseHTTPRequestHandler

class RequestHandler(HANDLER):

    def do_GET(self):
        if self.path == "/":
            response_code = 200
            content_type = 'text/html'
            message = "<h1>Hello from Python Web Server!</h1>"
            message += "<p>You requested the path: <strong>{}</strong></p>".format(self.path)
        elif self.path == "/about":
            response_code = 200
            content_type = 'text/html'
            message = "<h1>Hello from Python Web Server!</h1>"
            message += "<p>You are now on the about us page!!!</p>"
        else:
            response_code = 404
            content_type = 'text/html'
            message = "<h1>404 Not Found</h1>"
            message += "<p>The requested page <strong>{}</strong> does not exist.</p>".format(self.path)


        self.send_response(response_code)
        
        self.send_header = content_type
        self.end_headers()

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