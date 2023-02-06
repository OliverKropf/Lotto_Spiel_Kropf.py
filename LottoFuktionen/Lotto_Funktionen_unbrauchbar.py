import random


def bcolorsOK():
    oK = '\033[92m'
    return oK


def bcolorsFail():
    fAIL = '\033[91m'
    return fAIL


def bcolorsUser():
    uSER = '\033[95m'
    return uSER


def bcolorsReset():
    rESET = '\033[0m'
    return rESET


def allowedNumbers():
    allowed = [i for i in range(1, 46)]
    return allowed


def lottoTipsAndSpreading():
    userNumberList = []
    while True:
        tipsAnzahl = int(input("How often do you want to Tip?\n"))
        if 0 >= tipsAnzahl >= 12:
            print(bcolorsFail() + "Wrong Top-Input!" + bcolorsReset())
            continue
        else:
            i = 1
            while i <= tipsAnzahl:
                userNumberList.append(lottoNumberUser(i))
                if i == tipsAnzahl:
                    lottoNumberList = lottoNumberOutput()
                    counter = lottoNumberComparison(lottoNumberList, userNumberList[i])
                    lottoNumberPrintOutcome(counter)
                else:
                    i += 1
            break


def lottoNumberUser(i):
    numberCounter = 1
    print(i, "Tip:")
    i += 1
    allowed = allowedNumbers()
    userNumbersList = []
    if numberCounter >= 6:
        numberCounter -= 5
    else:
        while numberCounter <= 6:
            print("Type your", numberCounter, "lucky Number:")
            userNumbers = input()
            userNumbers = lottoFilter(userNumbers)
            userNumbers = isInputNumeric(userNumbers)
            if userNumbers in allowed:
                userNumbersList.append(userNumbers)
                allowed.remove(userNumbers)
                numberCounter += 1
                continue
            elif userNumbers in userNumbersList:
                print(bcolorsFail() + "Lucky number can't be the same as the number before!\n" + bcolorsReset())
                continue
            else:
                print(bcolorsFail() + "Your lucky number should be between 1 and 45!\n"
                                      "We are playing normal Lotto and nothing extravagant!" + bcolorsReset())
                continue
        newUserNumbersList = userNumbersList
        return newUserNumbersList


def lottoFilter(userNumbers):
    if len(userNumbers) >= 3:
        errorCode = 2
        errorFunction(errorCode)
    elif userNumbers == '0':
        errorCode = 3
        errorFunction(errorCode)
    else:
        return userNumbers


def isInputNumeric(userNumber):
    try:
        userNumberNew = int(userNumber)
        return userNumberNew
    except:
        errorCode = 1
        return errorFunction(errorCode)


def errorFunction(errorCode):
    if errorCode == 1:
        return print(bcolorsFail() + "Invalid Input!\n" + bcolorsReset())
    elif errorCode == 2:
        return print(bcolorsFail() + "Your lucky number is too long! Max: 2 digits!\n" + bcolorsReset())
    elif errorCode == 3:
        return print(bcolorsFail() + "Lucky number can't be 0!\n" + bcolorsReset())


def lottoNumberOutput():
    lottoNumberList = random.sample(range(1, 45), 6)
    extraNumber = random.sample(range(1, 45), 1)
    return lottoNumberList


def lottoNumberComparison(lottoNumberList, userNumberList):
    counter = 0
    for k in lottoNumberList:
        for j in userNumberList:
            if k == j:
                print(bcolorsOK() + "Your lucky number:", j, "was correct!\n" + bcolorsReset())
                counter += 1
    print(bcolorsOK() + "Today's lucky numbers are:" + bcolorsReset(), lottoNumberList)
    print(bcolorsUser() + "Your inputs were:" + bcolorsReset(), userNumberList)
    return counter


def lottoNumberPrintOutcome(counter):
    if counter == 1:
        print(bcolorsOK() + "You had:", counter, "correct guess!" + bcolorsReset())
    elif counter >= 2:
        print(bcolorsOK() + "You had:", counter, "correct guesses!" + bcolorsReset())
    else:
        print(bcolorsFail() + "Sadly you hit nothing!\nBetter luck next time!" + bcolorsReset())
