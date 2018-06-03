#!/usr/bin/python
import sys
import random

secretNumber = random.randint(1, 10)
counter = 0
exerciseMessageAnna = """Toen ik van 'Testautomatisering' hoorde, dacht ik: 'DAT wil ik. Dat WIL ik. Dat wil IK!' 

Tijdens de Masterclass mocht ik hiervan proeven en echt: dat smaakte naar meer! Ik mocht daarna testen uitvoeren voor 
Scouting Nederland en die kans greep ik: ik volgde een cursus 'C# voor testers' en leerde over Cucumber. Wat was ik 
trots toen ik mijn eerste eigen testscript losliet op de Scouting website en het nog bleek te werken ook. 

Bij NXP greep ik alles aan om testautomatisering te doen. Ik paste het Python script aan en in de ‘vrije’ uurtjes
praatte ik wat tegen de API (vriendelijke jongen). Helaas is dit niet genoeg om echt te worden wat ik wil zijn:
een echte testautomatiserings expert. Als ik mee mag doen aan de Bootcamp beloof ik plechtig me volledig in te zetten,
een extra tandje bij te zetten en zal ik nooit een ochtendhumeur meebrengen."""


def printExercise():
    message = exerciseMessageAnna
    return message

def selectQuestionMessage(argument):
    switcher = {
        0: """Hallo, ik ben Spoenk, Anna's Python Robot. Leuk om kennis te maken! Wil je graag haar motivatie 
lezen voor de Summer Automation Bootcamp? Typ dan een getal tussen de 1 en de 10 en druk op enter. 
Als je goed gokt, mag je haar motivatie lezen :) : """,
        1: "Helaas... Probeer het nog eens: ",
        2: "Laatste kans...: ",
        3: "Niet goed geraden, jammer! Maar ik ben de moeilijkste niet hoor. Druk op " + str(secretNumber) + " om door te gaan..."
    }
    return switcher.get(argument, "Niet goed geraden, jammer! Druk op " + str(secretNumber) + " om door te gaan...")

def inputNumber():
    number = input(selectQuestionMessage(counter))
    return number

def checkNumber(number):
    if number == str(secretNumber):
        return True
    else:
        return False

def guess():
    global counter
    number = inputNumber()
    check = checkNumber(number)
    if check:
        print(printExercise())
    else:
        counter += 1
        guess();

guess()