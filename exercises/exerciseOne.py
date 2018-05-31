#!/usr/bin/python
import sys
import requests

from motivationws.Requests import Requests
from util.StringFormat import StringFormat

wsEndpoint = 'http://localhost:5000'
ws = Requests(wsEndpoint)
welcomeMessage = ws.get_welcome_text()
welcomeAuthor = ws.get_welcome_author()
motivationMessage = ws.get_motivation_text()
motivationAuthor = ws.get_motivation_author()

def printWelcomeText():
    return StringFormat(welcomeMessage).create_paragraph()

def printWelcomeAuthor():
    return StringFormat(welcomeAuthor).create_author_format()

def printExercise():
    return StringFormat(motivationMessage).create_paragraph()

def printExerciseAuthor():
    return StringFormat(motivationAuthor).create_author_format()

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
print(printWelcomeAuthor())
print()
print(printExercise())
print(printExerciseAuthor())
