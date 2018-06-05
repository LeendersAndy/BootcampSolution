#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
motivationPart1 = "Zoals jullie weten geef ik training in API testen met Postman (dit noem ik altijd programmeren light), pruts wat met RestAssured en bouw samen met Robert en Michel aan een Framework. In dat framework zie ik echt pracht oplossingen van de hand van Michel, echt magnefiek! "
motivationPart2 = "Anyway, wat ik Michel (en misschien ook Robert een beetje :P) zie coderen, die oplossingen had ik niet kunnen vinden op Google met mijn huidige kennis. Omdat ik niet eens had kunnen bedenken dat te gaan zoeken op Google. En tevens als ik zo'n oplossing zie en ik kan hem hergebruiken, kan ik jullie nu niet eens vertellen wat ik bedoel, want ik weet niet hoe het heet! "
motivationPart3 = "Kortom, met de Bootcamp hoop ik veel nieuwe oplossingen te leren en er ook over te kunnen vertellen. Zodat ik me niet meer light voel, maar zelf verzekerd genoeg voor een intake voor een automatiseringsopdracht!"

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise(string):
    motivation = string
    return motivation

def numberOfWords(string):
    return len(string.split())

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")

def query_yes_no(question, prompt, feedbackYes, feedbackNo):

    validYes = {"1"}
    validNo = {"2"}

    while True:
        sys.stdout.write(question + "\n" + prompt + "\n Uw antwoord:  ")
        choice = raw_input().lower()
        if choice in validYes:
            print (feedbackYes)
            return False
        elif choice in validNo:
            print (feedbackNo)
            return False
        else:
            sys.stdout.write("Beetje de tester aan het uithangen? Kies gewoon 1 van de gegeven opties.\n")

def query_yes_yes(question, prompt, feedbackYes):

    validYes = {"Ja", "ja"}
    validNo = {"Nee", "nee"}

    while True:
        sys.stdout.write(question + "\n" + prompt + "\n Uw antwoord:  ")
        choice = raw_input().lower()
        if choice in validYes:
            print (feedbackYes)
            return False
        elif choice in validNo:
            sys.stdout.write("Heren, dat was geen optie.\n")
        else:
            sys.stdout.write("Beetje de tester aan het uithangen? Kies gewoon 1 van de gegeven opties.\n")

if len(welcomeMessage) != 91:
    sys.exit("Nice try, but not quite right :)")



# Actions in the console
print(printWelcomeText() + "\n")

if (numberOfWords(motivationPart1) + numberOfWords(motivationPart2) + numberOfWords(motivationPart3)) > 150:
    sys.exit("Sorry, je motivatie is te lang")

query_yes_no("Dank u heren. Hebben we er een beetje zin in dit te lezen?", "1. Ja \n2. Enorm! ik kijk al dagen uit naar de motivatie van onze meest geliefde Technische Unit collega die nog geen contract heeft getekend bij Valori!",  "Beetje meer enthousiasme mocht wel", "Dat dacht ik!")
print(printExercise(motivationPart1))
query_yes_no("Heb je zo genoeg veren in je reet Michel?", "1. Ja, dit is al ligt ongemakkelijk \n2. Nee, ga door, ga door!", "Geen dank", "Oke, je kunt ook super goed dingen uitleggen over Ghost Inspector met een Jan Jouke in je nek te hijgen!")
print(printExercise(motivationPart2))
query_yes_no("Toch benieuwd naar een voorbeeld met wat ik bedoel?", "1.Ja, Graag! \n2. Nee, we weten hoe goed Michel is, we get the point",
             "In het Framework: In de feature/Section-addSection, I want to add a section name <dataToBeEntered> to the Editie", "Terecht!")
print(printExercise(motivationPart3))
query_yes_yes("Ove2rtuigd?", "Ja of Ja", "Mooi, Michel, tot bij de Persgroep en Tim en William, tot bij de Bootcamp!")