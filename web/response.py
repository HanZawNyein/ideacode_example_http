import json


class Response:
    def response_plain_text(self, request, status_code=200, type="text/plain", message=...):
        request.send_response(status_code)
        request.send_header('Content-type', type)
        request.end_headers()
        request.wfile.write(message)

    def response_json(self, request, status_code=200, message=...):
        message = json.dumps(message).encode('utf-8')
        self.response_plain_text(request=request,
                                 status_code=status_code,
                                 type='application/json',
                                 message=message)


res = Response()
response_json = res.response_json
response_plain_text = res.response_plain_text
