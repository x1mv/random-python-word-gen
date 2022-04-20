## Random Word Generator by: x1mv ##
from time import sleep
import os
import random


## Start ##



while True: ## ask if the user wants to generate another word
    print("Types:  number, object, activity, guns")
    choosetype = input("Choose a word type from above: ")

## Words ##

    type_number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "four hundred ninety nine", "sixty nine", "four hundred twenty", "thirty two", "ninety two", "one hundred and twelve", "twenty one", "fifty five", "three hundred ten", "one hundred and twelve", "twelve thousand", "two point six million", "ninety one", "fourty seven", "thirty six"]
    type_object = ["women","computer", "brick", "pencil", "paper", "clock", "sunglasses", "desk", "chair", "scissors", "hat", "pen", "mask", "knife", "spoon", "fork", "mouse", "keyboard", "cardboardgod8", "remote", "ball", "headphone", "speaker", "microphone", "monitor", "calculator", "flash drive", "car", "bike", "skateboard", "can", "toy", "helmet", "armour", "vest", "plush", "newspaper", "box", "gaming console", "led light", "window", "glass", "heater", "usb", "charger", "money", "cd", "dvd", "battery"]
    type_guns = ["AR-15", "Glock 18", "Glock 17", "M16", "M4", "AAC Honey Badger", "AK203", "AK205", "AK-47", "AK-74", "FAMAS", "Galil", "MK 556", "Five-seven", "Glock 19", "Glock 19X", "Heckler & Koch P2000", "MAC-10", "Makarov", "MAC-11", "MP9", "M1911", "Caracal Pistol (i had to include it)", "L96A1", "Dragunov SVU", "MK 13", "KRISS Vector", "PP-19 Bizon", "SIG MPX", "Steyr AUG PARA", "Browning Hi-Power", "Desert Eagle", "Beretta M9", "SIG P250", "BFG 50"]
    type_activity = ["excercising", "speaking", "playing", "coding", "running", "shooting", "farming", "talking", "fighting", "spraying", "crying", "chatting", "laughing", "farting", "showering", "questioning", "driving", "tanking", "working", "rewiring", "plugging", "cooking", "eating", "fishing", "buying", "breaking", "writing", "selling", "listening", "drinking", "watering", "shitting", "pissing", "cumming", "smoking", "destroying", "dressing", "faking", "trying", "doing", "farting"]
    ## this took way too long LMAO

## the word choice ##

    number_pfunc = random.choice(type_number)
    object_pfunc = random.choice(type_object)
    guns_pfunc = random.choice(type_guns)
    activity_pfunc = random.choice(type_activity)

## main part ##
    if choosetype == "number":
        print(" ")
        print(number_pfunc)
    elif choosetype == "object":
        print(" ")
        print(object_pfunc)
    elif choosetype == "activity":
        print(" ")
        print(activity_pfunc)
    elif choosetype == "guns":
        print(" ")
        print(guns_pfunc)

    ## restart script ##
    print(" ")
    regen = input("Generate again? (Y/N): ")
    if regen.lower() != "y":
        print(" ")
        break
