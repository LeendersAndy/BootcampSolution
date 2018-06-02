#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
exerciseMessageAnna = """Toen ik van 'Testautomatisering' hoorde, dacht ik: 'DAT wil ik. Dat WIL ik. Dat wil IK!' 

Tijdens de Masterclass mocht ik hiervan proeven en echt: dat smaakte naar meer! Ik mocht daarna testen uitvoeren voor 
Scouting Nederland en die kans greep ik: ik volgde een cursus 'C# voor testers' en leerde over Cucumber. Wat was ik 
trots toen ik mijn eerste eigen testscript losliet op de Scouting website en het nog bleek te werken ook. 

Bij NXP greep ik alles aan om testautomatisering te doen. Ik paste het Python script aan en in de ‘vrije’ uurtjes
praatte ik wat tegen de API (vriendelijke jongen). Helaas is dit niet genoeg om daar te komen waar ik wil zijn:
een echte testautomatiserings expert. Als ik mee mag doen aan de Bootcamp beloof ik plechtig me volledig in te zetten,
een extra tandje bij te zetten en zal ik nooit een ochtendhumeur meebrengen."""

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    message = exerciseMessageAnna
    return message

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

print(printExercise())
