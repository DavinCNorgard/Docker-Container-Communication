import requests

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class WeatherServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        url = self.parse_url()
        params = self.parse_params(url.query)
        if 'latitude' in params and 'longitude' in params:
            lat = params['latitude'][0]
            lon = params['longitude'][0]
            weather = self.get_weather(lat, lon)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(weather, 'utf-8'))
        else:
            print('missing lat and lon perameters')

    
    def parse_url(self):
        return urlparse(self.path)
    
    def parse_params(self, query):
        return parse_qs(query)
    
    def get_weather(self, lat, lon):
        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_weather = data['current_weather']
            return f'The current weather at ({lat}, {lon}) is {current_weather}'
        else:
            return 'Unable to retrieve current weather.'

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    server = HTTPServer((host, port), WeatherServer)
    print(f'Started server at {host}:{port}')
    server.serve_forever()
