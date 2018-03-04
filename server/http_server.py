import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class CallbackServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.send_header("Access-Control-Allow-Origin", "*");
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        self.end_headers()

        response = {'status': 200,
                    'results':
                        [
                            {
                                'name': 'sushi', 'age': 33
                            },
                            {
                                'name': 'ohagi', 'age': 32
                            }
                        ]
                    }
        response_data = json.dumps(response)
        self.wfile.write(response_data.encode('UTF-8'))


if __name__ == '__main__':
    server = HTTPServer(('', 9000), CallbackServer)
    server.serve_forever()


