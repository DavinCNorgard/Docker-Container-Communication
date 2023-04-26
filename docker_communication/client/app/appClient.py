import requests

def send_get():

    lat = 19.22 #chosen randomly
    lon = 69.87 #chosen randomly

    url = f'http://localhost:5000/?latitude={lat}&longitude={lon}'

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)


send_get()
