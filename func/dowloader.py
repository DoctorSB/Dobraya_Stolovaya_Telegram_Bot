import requests

class Dowloader:
    def __init__(self, url, method='GET'):
        self.url = url
        self.method = method

    def get_html(self):
        response = requests.get(self.url)
        return response.text
