import requests
from configuration import Configuration

confjson = Configuration.load_json('config.json')
key = confjson.key

def get_weather():

    city_id = confjson.cityId
    url = 'https://api.openweathermap.org/data/2.5/weather'
    r = requests.get(url, params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': key})
    data = r.json()
    conditions = data['weather'][0]['description']
    temp = data['main']['temp']
    wind = data['wind']['speed']
    message = f'Погода в Новокузнецке: \n%s \nТемпература: %s°С \nСкорость ветра: %s m/s' % (conditions, temp, wind)
    return message

