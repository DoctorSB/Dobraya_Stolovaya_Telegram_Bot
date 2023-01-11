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
        print(names['class'][0])
        data = {}
        cur_key = ''
        while names.find_next_sibling('tr'):

            if 'table__area' in names['class']:
                cur_key = names.text
                # print(cur_key, end=' ')
                data[cur_key] = []
            else:
                data[cur_key] += [names['data-name']]

            # print(names['class'])
            names = names.find_next_sibling('tr')
        print(data)


if __name__ == '__main__':
    url = 'https://dobraya.su/menu/'
    dowloader = Dowloader(url)
    html = dowloader.get_html()
    parser = Parser(html).parse()
    # print(parser)
