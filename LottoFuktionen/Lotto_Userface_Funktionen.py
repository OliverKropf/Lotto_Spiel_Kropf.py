import random


def allowedNumbers():
    allowed = [i for i in range(1, 46)]
    return allowed


def getLottoNumbers():    # Übergabe der Lotto-Ziehung + Zusatzzahl
    lotteryList = lottoLuckyNumbers()
    return lotteryList


def lottoLuckyNumbers():   # Lotto-Ziehung + Zusatzzahl
    lottoNumberList = random.sample(range(1, 45), 7)
    return lottoNumberList


def numberRangeCheck(userList):   # Absicherung Range 1 - 45
    for i in range(6):
        if userList[i] <= 0 or userList[i] >= 46:
            errorCheck = 2
            return errorCheck
        else:
            continue
    # errorCheck = numberDoubleCheck(userList)
    errorCheck = 0
    return errorCheck


def numberDoubleCheck(userList):   # Absicherung auf doppelte Zahlen !FUNKTIONIERT NOCH NICHT!
    if len(userList) == 6:
        userList1 = userList[0:6]
        userList1 = set(userList1)
        listCheck(userList1)
    elif len(userList) == 12:
        userList2 = userList[6:12]
        userList2 = set(userList2)
        listCheck(userList2)
    elif len(userList) == 18:
        userList3 = userList[12:18]
        userList3 = set(userList3)
        listCheck(userList3)
    elif len(userList) == 24:
        userList4 = userList[18:24]
        userList4 = set(userList4)
        listCheck(userList4)


def listCheck(checkList):
    if len(checkList) != 6:
        errorCheck = 1
    else:
        errorCheck = 0
    return errorCheck


def lottoComparison(userList):   # Überprüfung ob Tips mit Lotto-Ziehung übereinstimmen
    lotteryList = getLottoNumbers()
    counter = 0
    for i in userList:
        for j in lotteryList:
            if i == j:
                counter += 1
    if counter == 0:
        checkSumOfList = 'Sie haben keine Zahl richtig geraten!\nHeutige Lotto-Ziehung: {}\nZusatzzahl: {}'.format(lotteryList[0:6], lotteryList[6])
    elif counter == 1:
        checkSumOfList = 'Sie haben {} Zahl richtig geraten!\nHeutige Lotto-Ziehung: {}\nZusatzzahl: {}'.format(counter, lotteryList[0:6], lotteryList[6])
    else:
        checkSumOfList = 'Sie haben {} Zahlen richtig geraten!\nHeutige Lotto-Ziehung: {}\nZusatzzahl: {}'.format(counter, lotteryList[0:6], lotteryList[6])
    return checkSumOfList   # Return der Vergleichs-Ausgabe in einer von mir gewählten Form


def listClearing(userList):
    for i in range(6):
        userList.pop()
