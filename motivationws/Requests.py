import requests


class Requests:
    """A class used to retrieve messages from
    an attempted webservice."""

    welcome_route = '/welcome'
    motivation_route = '/motivation'

    def __init__(self, base_url):
        self.base_url = base_url

    def get_welcome_text(self):
        return requests.get(self.base_url + self.welcome_route).json()['message']

    def get_motivation_text(self):
        return requests.get(self.base_url + self.motivation_route).json()['message']

    def get_welcome_author(self):
        return requests.get(self.base_url + self.welcome_route).json()['author']

    def get_motivation_author(self):
        return requests.get(self.base_url + self.motivation_route).json()['author']