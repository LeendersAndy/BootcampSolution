#!/usr/bin/python
import sys

motivation = "Mijn naam is Sören Veestraeten. Ondertussen ben ik 16 maanden aan het werk als software tester. Tot nu toe heb ik bij mijn klanten altijd manuele testen uitgevoerd. Mijn interesse ligt echter in test automation. Ik ben veel tijd aan het steken om van mezelf een meer technischer profiel te maken. Door mijn interesse weet ik er enkele dingen over, maar ik heb het gevoel dat ik nog essentiële kennis mis. Deze opleiding kan me hier zeker mee helpen. Daarna zou ik heel graag al de vergaarde kennis van de cursus willen toepassen op een project. Ik ben een heel gemotiveerd persoon die alles uit mezelf wil halen. Naar mijn gevoel zit test automation in mijn lichaam, maar moet iemand me nog helpen om het eruit te kunnen halen. Ik ben ervan overtuigd dat dit na de bootcamp gebeurd zal zijn! PS: Er staan twee schrijffouten in de opdracht."

def printExercise():
    return motivation

if len(motivation.split())>150:
    sys.exit("Sorry, jouw motivatie mag maximaal 150 woorden bevatten.")

print(printExercise())

