#!/usr/bin/python
import xml.etree.ElementTree as ET
import json
import requests

api_url_base = "https://sheetsu.com/apis/v1.0su/"


def run_exercise():
    if validate_length_of_text():
        print_motivation()
    else:
        print_error_text()


def validate_length_of_text():
    """
    Validate that the suggested amount of words is met
    """
    return len(get_motivation_text().split()) > 91


def print_motivation():
    print(get_motivation_text())


def print_error_text():
    print(get_error_text())


def get_motivation_text():
    """
    The motivation text is retrieved from the .XML
    :return:
    motivation_text
    """
    return ET.parse('motivation.xml').getroot()[0].text


def get_error_text():
    """
    Not sure how long the api endpoint will live for since it is hosted bij sheetsu.com
    The endpoint will return a list with one dictionary, in this dict you'll find the error message
    :return:
    error_text
    """
    api_url = api_url_base + '937356562c06'
    response = requests.get(api_url)

    if response.status_code == 200:
        error_text = json.loads(response.content.decode('utf-8'))
        return error_text[0]['text']
    else:
        return None


run_exercise()
