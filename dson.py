import requests
import json

class Data:
    def __init__(self, data):
        with open(data, 'r') as file:
            self.data = json.load(file)
        