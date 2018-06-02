#!/usr/bin/python
from motivationws.Requests import Requests
from util.StringFormat import StringFormat
from util.SizeCheck import check_if_length_exceeds, check_if_length_equals

ws_endpoint = 'http://localhost:5000'
ws = Requests(ws_endpoint)
welcome_message = ws.get_welcome_text()
welcome_author = ws.get_welcome_author()
motivation_message = ws.get_motivation_text()
motivation_author = ws.get_motivation_author()


def print_welcome_text():
    return StringFormat(welcome_message).create_paragraph()


def print_welcome_author():
    return StringFormat(welcome_author).create_author_format()


def print_exercise():
    return StringFormat(motivation_message).create_paragraph()


def print_exercise_author():
    return StringFormat(motivation_author).create_author_format()


check_if_length_equals(welcome_message, 91)
check_if_length_exceeds(motivation_message.split(), 150)

print(print_welcome_text())
print(print_welcome_author())
print()
print(print_exercise())
print(print_exercise_author())
