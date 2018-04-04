from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow

default_cow = cow.Ghostbusters()
print('Egon, this reminds me of the time you tried to drill a hole through your head.')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """sets up the http server from http.server base class"""
    def do_GET(self):
        """handles route for GET requests"""
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'<a href="/cowsay">Cowsay</a>')
            return

        elif parsed_path.path == '/test':
            try:
                cat = json.loads(parsed_qs['category'][0])
            
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'You did a bad thing')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'we did the thing with the qs')
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')    

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.send_response_only() 

    
def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server() 

    try:
        print('started server at port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.sever_close()


if __name__ == '__main__':
    run_forever()
