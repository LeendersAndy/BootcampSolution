#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
motivationMessage = " Waarde heren, \n \n Na ruim anderhalf jaar bezig geweest te zijn met de wat functionelere kant van het testvak, gaat het toch wel aardig kriebelen om ook het technische facet wat meer te verkennen. \n Mijn ambitie is vanaf dag 1 al geweest om me op termijn bezig te gaan houden met het automatiseren van testscripts. \n Nu ik me comfortabel genoeg voel bij het functionele testen, lijkt het me dat de tijd hier nu rijp voor is om verder te kijken. \n Bij mijn vorige klant was er amper ruimte om al wat automation toe te passen, en de omgeving was hier ook te complex om dit op een volwassen manier op te zetten. \n Mijn huidige klant heeft echter wel ruimte hiervoor en ik hoop dat de bootcamp me de kickstart geeft om hier mee aan de slag te gaan. \n \n Met vriendelijke groeten, \n \n Jeremy "

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    motivation = motivationMessage
    return motivation

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

#print(printWelcomeText())

print(printExercise())