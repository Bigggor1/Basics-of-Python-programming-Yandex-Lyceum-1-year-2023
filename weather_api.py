import requests
import json


def weather_by_ll(ll):
    lat = ll.split(',')[0]
    lon = ll.split(',')[1]
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={lat}&lon={lon}&[lang=ru_RU]'
    yandex_req = requests.get(url_yandex, headers={'X-Yandex-API-Key': '31edec50-cbef-4e12-a56f-8414eb65f234'},
                              verify=False)
    yandex_json = json.loads(yandex_req.text)
    return {'image': f'https://yastatic.net/weather/i/icons/funky/dark/{yandex_json['fact']['icon']}.svg',
            'temp': yandex_json['fact']['temp'], 'feels_like': yandex_json['fact']['feels_like']}
