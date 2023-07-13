import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(level=logging.INFO)


def run(host, port, handler=BaseHTTPRequestHandler, http_server=HTTPServer):
    server = http_server((host, port), handler)
    logging.info(f"Starting server at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run(host="localhost", port=8000)
