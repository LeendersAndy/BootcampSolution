#!/usr/bin/python
import sys
import textwrap

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
motivationText = "Met mijn huidige kennis ben ik instaat om scripts te schrijven en nu ben ik klaar voor de volgende stap. Door deel te nemen aan de bootcamp wil ik een aantal gestelde doelen behalen. Door zelfstandig een testframework op te kunnen zetten, verhoog ik naast mijn persoonlijke kwaliteiten ook die van Polteq. Met de technische kennis uit de bootcamp ben ik beter instaat om een professionele bijdrage te leveren aan (nieuw op te zetten) projecten binnen mijn huidige en toekomstige opdrachten. Door deze persoonlijke ontwikkeling ga ik voorbereid de toekomst tegemoet. Daarnaast lijkt het me ook ontzettend leuk om jonge, nieuwe medewerkers te kunnen begeleiden, inspireren en enthousiast te maken voor testautomatisering."
errorMessageWelcome = "Nice try, but not quite right :)"
errorMessageMotivation = "You are writing a motivation, not a book ;). Use max 150 words."
# To avoid "magic" numbers
maxCharactersPerLine = 130
charactersLength = 91
maxWordsMotivation = 150


def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    motivation = textwrap.fill(motivationText, width=maxCharactersPerLine)
    return motivation

if len(welcomeMessage) != charactersLength:
    sys.exit(errorMessageWelcome)

if len(motivationText.split()) > maxWordsMotivation:
    sys.exit(errorMessageMotivation)
    
print(printExercise())