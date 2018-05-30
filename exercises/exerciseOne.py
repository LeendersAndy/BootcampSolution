#!/usr/bin/python
import sys
import requests

wsEndpoint = 'http://localhost:5000'
welcomeMessage = requests.get(wsEndpoint + '/welcome').json()['message']
motivation = requests.get(wsEndpoint + '/motivation').json()['message']

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    return motivation

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
print(printExercise())
