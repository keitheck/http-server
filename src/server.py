from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow

print('Egon, this reminds me of the time you tried to drill a hole through your head.')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """sets up the http server from http.server base class"""
    def do_GET(self):
        """handles route for GET requests"""
        parsed_path = urlparse(self.path)
        # print('parsed path {} => '.format(parsed_path))
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()
            """https://docs.python.org/3/tutorial/inputoutput.html"""
            with open('index.html') as f:
                fdata = f.read()
                self.wfile.write(fdata.encode('utf8'))
            return

        elif parsed_path.path == '/cowsay':
            """handles endpoint cowsay"""
            cheese = cow.Moose(thoughts=True)
            msg = cheese.milk("I have a hole in my head")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode('utf8'))
            return

        elif parsed_path.path == '/cow':
            """handles endpoint cow and parses msg=xxxx from url"""
            cheese = cow.Moose(thoughts=True)

            try:
                msg = json.loads(parsed_qs['msg'][0])
            except json.decoder.JSONDecodeError:    
                msg = parsed_qs['msg'][0]
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad Request | 400')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(cheese.milk(msg).encode('utf8'))
            return    

        else:
            """404"""
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')    

    def do_POST(self):
        """post returns json of message"""
        parsed_path = urlparse(self.path)
        # parsed_qs = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/cow':
            
            try:
                content_length = int(self.headers['Content-Length'])
                body = json.loads(self.rfile.read(content_length).decode('utf8'))
            
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad Request | 400')
                return

        cheese = cow.Moose(thoughts=True)
        msg = cheese.milk(body['msg'])

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'content': msg}).encode('utf8'))
        return


def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server() 

    try:
        print('started server at port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
