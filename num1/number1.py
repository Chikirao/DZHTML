import requests
from pprint import pprint

# Создадим функцию для подсчёта интелекта
def heroe_int(hero_name):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    jsdict = requests.get(url).json()
    for hero in jsdict:
        if hero_name == hero.get("name"):
            return hero.get("powerstats").get("intelligence")

heroes_with_int ={
    heroe_int('Hulk'): 'Hulk',
    heroe_int('Captain America'): 'Captain America',
    heroe_int('Thanos'): 'Thanos',
}

print('Самый умный -', heroes_with_int.get(max(heroes_with_int.keys())), '\nЕго интелект =', max(heroes_with_int.keys()))