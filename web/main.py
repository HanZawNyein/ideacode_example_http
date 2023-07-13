from http.server import HTTPServer
import logging
from dispatch import MyHandler
import server

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000
    server.run(HOST, PORT, handler=MyHandler)
    # server = HTTPServer((HOST, PORT), MyHandler)
    # logging.info(f"Starting server at http://{HOST}:{PORT}")
    # server.serve_forever()
