import bs4 as bs
import requests
import json
from dowloader import Dowloader

class Parser:

    def __init__(self, sourse):
        self.sourse = sourse
    
    def parse(self):
        soup = bs.BeautifulSoup(self.sourse, 'html.parser').find('table', class_='table table__menu')
        names = soup.find_all('tr')[1]
        
        # for tr in names:
        print(names)
        
       
        

if __name__ == '__main__':
    url = 'https://dobraya.su/menu/'
    dowloader = Dowloader(url)
    html = dowloader.get_html()
    parser = Parser(html).parse()
    # print(parser)