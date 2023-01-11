import bs4 as bs
import requests
import json
from dowloader import Dowloader


class Parser:

    def __init__(self, sourse):
        self.sourse = sourse

    def parse(self):
        soup = bs.BeautifulSoup(self.sourse, 'html.parser').find(
            'table', class_='table table__menu')
        names = soup.find_all('tr')[1]

        # for tr in names:
        data = {}
        cur_key = ''
        while names.find_next_sibling('tr'):

            if 'table__area' in names['class']:
                cur_key = names.text[1:len(names.text)-1].lower()
                # print(cur_key, end=' ')
                data[cur_key] = []
            else:
                data[cur_key] += [{'Название': names.find_all('td')[0].text.lower(),  # тут получаем название позиции и записываем с маленькой буквы
                                   'Выход, гр': names.find_all('td')[1].text,
                                   'Завтрак': names.find_all('td')[2].text,
                                   'Обед': names.find_all('td')[3].text,
                                   'Ужин': names.find_all('td')[4].text,
                                   'Ккал': names.find_all('td')[5].text}]

            # print(names['class'])
            names = names.find_next_sibling('tr')
        return json.dumps(data, indent=4, ensure_ascii=False)

    def save(self):
        with open('menu.json', 'w') as file:
            file.write(self.parse())
