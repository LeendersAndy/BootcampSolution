#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
motivationText = "Motivatie.txt"
numberOfWords = 0


def printWelcomeText():
    welcome = welcomeMessage
    return welcome


def printExercise():
    file = open(motivationText, "r")
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
    file.close()


with open(motivationText, 'r') as file:
    for line in file:
        wordsList = line.split()
        numberOfWords += len(wordsList)

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

if numberOfWords > 150:
    sys.exit("Nice try, but your motivation is too long! So it is boring everyone!")

print(printWelcomeText())
printExercise()