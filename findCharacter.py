#!/usr/bin/env python3
def findCharacter(textOne, textTwo):
    
    textList = []

    for char in textTwo:
        textList.append(char.upper())

    for char in textOne.upper():
        if char in textList:
            onTheList = True
        else:
            onTheList = False
    
    if textTwo.find(textOne) != -1:
        print("The word "+"["+textOne+"]"+" it's on the list")
    else:
        print("The word "+"["+textOne+"]"+" not on the list")

    if onTheList == True:
        print(textOne,"all characters are in the list")
    else:
        print(textOne,"a character is not in the list")

findCharacter("donor", "NabucodonosORdono")