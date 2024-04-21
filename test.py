import pygame
import os
import requests
import json


def toponym_by_geocode(geocode):
    yandex_req = requests.get(
        f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={geocode}&lang=en_US'
        f'&format=json')
    yandex_json = yandex_req.json()

    toponym = yandex_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]
    toponym_coodrinates = toponym["Point"]["pos"]

    return {'address': toponym_address, 'cords': toponym_coodrinates.replace(' ', ',')}


def urlImage_by_ll(ll):
    yandex_req = requests.get(
        f'http://static-maps.yandex.ru/1.x/?ll={ll}&spn=10,1&size=600,300&l=map&pt={toponym['cords']},flag')

    return yandex_req.url


def weather_by_ll(ll):
    lat = ll.split(',')[0]
    lon = ll.split(',')[1]
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={lat}&lon={lon}&[lang=ru_RU]'
    yandex_req = requests.get(url_yandex, headers={'X-Yandex-API-Key': '31edec50-cbef-4e12-a56f-8414eb65f234'},
                              verify=False)
    yandex_json = json.loads(yandex_req.text)
    return {'image': f'https://yastatic.net/weather/i/icons/funky/dark/{yandex_json['fact']['icon']}.svg',
            'temp': yandex_json['fact']['temp'], 'feels_like': yandex_json['fact']['feels_like']}