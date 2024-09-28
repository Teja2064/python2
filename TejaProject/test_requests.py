from http.server import BaseHTTPRequestHandler, HTTPServer

class ServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Check if the request payload contains characteristics of Spring4Shell exploitation
        if 'tomcatwar.jsp' in post_data and 'pwd=j' in post_data and 'cmd=' in post_data:
            # If the request matches the pattern, block it
            self.send_error(403, "Forbidden")
            print("Blocked an attempt to exploit Spring4Shell vulnerability")
        else:
            # If the request does not match the pattern, allow it
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))


host = "localhost"
port = 8000

if __name__ == "__main__":
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
