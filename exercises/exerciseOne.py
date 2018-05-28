#!/usr/bin/python
import sys

motivationMessage = "\b Hallo heren, mijn naam is Freek Ruskus en ik wil graag de kant van het technisch testen opgaan. \n Eind Juni loopt mijn huidige opdracht af en ik heb inmiddels te horen gekregen dat ik potentieel een technische opdracht kan gaan overnemen. \n Deze opdracht blijkt van vrij hoog niveau te zijn, en momenteel heb ik enkel de technische kennis die ik tijdens de Masterclass heb opgedaan tot mijn beschikking. \n Via de Summer Automation Bootcamp zou ik een veel sterkere kennisbasis kunnen opdoen die ik dan ook meteen kan inzetten bij deze nieuwe opdracht. \n"

def printExercise():
    motivation = motivationMessage
    return motivation

if len(motivationMessage.split()) > 150:
    sys.exit("\b motivationalMessage is too long. Max 150 words.")

print(printExercise())
