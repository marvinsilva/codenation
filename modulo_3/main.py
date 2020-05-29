import requests


def get_temperature(lat, lng):
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = f'https://api.darksky.net/forecast/{key}/{lat},{lng}'
    response = requests.get(url)
    data = response.json()
    temperature = data.get('currently').get('temperature')
    if not temperature:
        return
    return int((temperature - 32) * 5.0 / 9.0)
