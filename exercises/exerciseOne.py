#!/usr/bin/python
import sys
import time
import textwrap

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"

#onderstaande motivatie heb ik omwille van de opdracht en de leesbaarheid op deze manier hard coded ingevoerd


motivationText = """Dit jaar bij Polteq begonnen in de masterclass, en ik wil direct doorpakken en mezelf specialiseren.
Voordat ik bij Polteq kwam heb ik vooral gekeken naar functies in de (software) development. Ik heb daar geen achtergrond in, maar ben ongeveer een jaar geleden begonnen met Python en nu Java,
hoewel ik eerlijk moet toegeven dat het best taai is om hier grote stappen in te maken zonder input van buitenaf en na eerder een andere carrière gevolgd te hebben.
Het mooie is dat dit terugkomt in testautomation en zodoende ben ik sowieso vastbesloten deze richting op te gaan, met of zonder de bootcamp. Nog voordat de oproep tot inschrijving voor de bootcamp langskwam was ik al bezig met testautomation.
Echter geef ik toe dat mijn ontwikkeling hierin vrij langzaam gaat en ik de kans van de bootcamp daarom dolgraag aangrijp om hier een degelijke basis in te leggen!"""

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    #linelength 100 is gekozen voor leesbaarheid, maar kan elke lengte hebben
    motivation = (textwrap.fill(motivationText, 100))
    return motivation

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

#onderstaande command heb ik uitgeschakeld zodat welcomeMessage niet wordt meegeprint tijdens runnen van de code
#print(printWelcomeText())

while True:
    print("Ben je benieuwd naar de motivatie van Dennis...?")
    time.sleep(2)
    question = input("Typ ja of nee: ")
    question = question.lower()
    if question == "ja":
        print("Mooi!")
        time.sleep(1)
        print("Daar komt ie dan...:\n")
        time.sleep(2)
        print(printExercise())
        break
    elif question == "nee":
        print("Ik heb nog wel zó mijn best gedaan om gemotiveerd over te komen :D")
        break
    else:
        print("Antwoorden met JA of NEE graag :)")
        time.sleep(2)