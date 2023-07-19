import json
from jinja2 import FileSystemLoader, Environment
from http.server import BaseHTTPRequestHandler
from response import response_plain_text
from routes import url_pattern, post_url_pattern


class MyHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.template_env = Environment(loader=FileSystemLoader('templates'))
        super().__init__(*args, **kwargs)

    def render_template(self, template_name, **kwargs):
        template = self.template_env.get_template(template_name)
        body = template.render(kwargs).encode('utf-8')
        return response_plain_text(self, 200, type='text/html', message=body)

    def do_GET(self):
        optional_parameters = dict()
        if '?' in self.path:
            data = self.path.rsplit('?')
            self.path = data[0]
            data = data[1].split('&')
            for d in data:
                _ = d.split('=')
                optional_parameters[_[0]] = _[1]
        if self.path in url_pattern:
            url_pattern[self.path](self, **optional_parameters)
        else:
            response_plain_text(request=self, status_code=404, message=b'404 not Found.')

    def do_POST(self):
        if self.path in post_url_pattern:
            content_length = int(self.headers['Content-Length'])
            request_body = self.rfile.read(content_length).decode('utf-8')
            request_body = json.loads(request_body)
            post_url_pattern[self.path](self, **request_body)
        else:
            response_plain_text(request=self, status_code=404, message=b'404 not Found.')
