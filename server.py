import http.server
import socketserver
from urllib.parse import urlparse
import os

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # На любой GET-запрос возвращаем contacts.html
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Читаем HTML из файла через open()
        with open(os.path.join('templates', 'contacts.html'), 'r', encoding='utf-8') as f:
            content = f.read()

        self.wfile.write(content.encode('utf-8'))


# Запуск сервера
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()