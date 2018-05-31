import requests


class Requests:
    """A class used to retrieve messages from
    an attempted webservice."""

    welcomeRoute = '/welcome'
    motivationRoute = '/motivation'

    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def get_welcome_text(self):
        return requests.get(self.baseUrl + self.welcomeRoute).json()['message']

    def get_motivation_text(self):
        return requests.get(self.baseUrl + self.motivationRoute).json()['message']

    def get_welcome_author(self):
        return requests.get(self.baseUrl + self.welcomeRoute).json()['author']

    def get_motivation_author(self):
        return requests.get(self.baseUrl + self.motivationRoute).json()['author']