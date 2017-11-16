#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"

motivatieTekst = """
\n\033[1mStructuur leren aanbrengen.\033[0m
Hoewel al in een aantal automatiseringsprojecten betrokken wil ik in deze bootcamp leren bij testautomatiseren een goede structuur aan te brengen en te handhaven. Mijn valkuil daarbij was vaak dat er geen collegiale review beschikbaar was (of niet gezocht is) zodat oplossingen wel werkten maar uiteindelijk niet simpel overdraagbaar, onderhoudbaar en onduidelijk van structuur waren.
\n\033[1mGebruik keywords en frameworks\033[0m
Ook de keuze voor en het gebruik van testframeworks wil ik graag ervaren. Met name zoek ik manieren om technische en functionele code te (onder)scheiden. Hierbij wil ik me niet alleen op HTTP-protocollen richten maar ook op andere manieren om applicaties te benaderen.
\n\033[1mProgrameerkennis\033[0m
Persoonlijk levert dit ook een motivering op om minimaal java of python wat beter beheersen.
"""

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    motivatie = motivatieTekst
    return motivatie


if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

if len(motivatieTekst) != 0:
    print(printExercise())
else:
    print(printExercise())