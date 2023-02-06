import random


def bcolorsFail():
    fAIL = '\033[91m'
    return fAIL


def bcolorsReset():
    rESET = '\033[0m'
    return rESET


def quantityTips():
    try:
        quantityTips = tipCheck()
        return quantityTips
    except:
        print(bcolorsFail() + "Please choose with how many tips you want to play!\n" + bcolorsReset())


def tipCheck():   # Tip-Auswahl mit Absicherung/Fehlermeldung
    while True:
        try:
            tips = int(input("Choose how many tips you want to play:\n"))
            if tips >= 13 or tips <= 0:
                print(bcolorsFail() + "Wrong Tip-Input!\nYou can choose between 1 - 12 Tips!" + bcolorsReset())
                continue
            else:
                return tips
        except:
            print(bcolorsFail() + "Wrong Input! You can only use Integers!\n" + bcolorsReset())


def numberInput():   # Zahlenauswahl mit Absicherungen/Fehlermeldungen
    userTip = []
    print("Please type 6 numbers between 1 - 45: ")
    while len(userTip) < 6:
        try:
            newUserInput = int(input())
            if newUserInput in userTip:
                print(bcolorsFail() + "Choose a bew Number!", newUserInput, "has already been used!\n" + bcolorsReset())
            elif newUserInput < 1 or newUserInput > 45:
                print(bcolorsFail() + "You can choose between 1 - 45! Nothing else is allowed!\n" + bcolorsReset())
            elif userTip.append(newUserInput):
                userTip.sort()
        except:
            print(bcolorsFail() + "Wrong Input! You can only use Integers!\n" + bcolorsReset())

    return userTip


def lottoLuckyNumbers():   # Lotto-Ziehung
    lottoNumberList = random.sample(range(1, 45), 6)
    return lottoNumberList


def extraLuckyNumber():   # Zusatzzahl
    extraNumber = random.randint(1, 45)
    return extraNumber


def lottoComparison(myTips, lotteryNumbers):   # Überprüfung ob Tips mit Lotto-Ziehung übereinstimmen
    counter = 0
    for i in myTips:
        for j in lotteryNumbers:
            if i == j:
                counter += 1
    return counter