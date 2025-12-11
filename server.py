import http.server # Handling raw request and parsing
import socketserver # Handling TCP Connections]
import os
import mimetypes

PORT = 8000
STATIC_DIR = 'static'
HANDLER = http.server.BaseHTTPRequestHandler

mimetypes.init()

class RequestHandler(HANDLER):

    def do_GET(self):
        requested_path = self.path
        if requested_path == "/":
            file_name = 'index.html'
        else:
            file_name = requested_path[1:]

        file_path = os.path.join(STATIC_DIR, file_name)

        if os.path.isfile(file_path):
            
            try:
                with open(file_path, 'rb') as f:
                    file_content = f.read()

                    mime_type, _ = mimetypes.guess_type(file_path)
                    if mime_type == None:
                        mime_type = "application/octet-stream"

                    self.send_response(200)
                    self.send_header('Content-type', mime_type)
                    self.send_header('Content-Length', len(file_content))
                    self.end_headers()
                    
                    self.wfile.write(file_content)
            
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Internal Server Error: " + str(e).encode('utf8'))


        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            message = "<h1>404 Not Found</h1><p>File not found at: <strong>{}</strong></p>".format(file_path)
            self.wfile.write(bytes(message, "utf8"))


with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopping...")
        httpd.server_close()