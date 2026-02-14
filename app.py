from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # На любой GET-запрос возвращаем страницу "Контакты"
        file_path = os.path.join('templates', 'contacts.html')
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(file_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()