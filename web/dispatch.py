from http.server import BaseHTTPRequestHandler
import views
from response import response_plain_text
from routes import url_pattern

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path in url_pattern:
            url_pattern[self.path](self)
        else:
            response_plain_text(request=self, status_code=404, message=b'404 not Found.')
            # self.send_response(404)
            # self.send_header('Content-type', 'text/plain')
            # self.end_headers()
            # self.wfile.write(b'404 not Found.')

        #
        # self.send_response(200)
        # self.send_header('Content-type', 'text/plain')
        # self.end_headers()
        # self.wfile.write(b'THis is Home')
