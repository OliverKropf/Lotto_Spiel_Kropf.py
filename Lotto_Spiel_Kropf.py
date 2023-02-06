from LottoFuktionen import Lotto_Funktionen_V2


def bcolorsOK():
    oK = '\033[92m'
    return oK


def bcolorsBackGround():
    bACKGROUND = '\033[93m'
    return bACKGROUND


def bcolorsUser():
    uSER = '\033[95m'
    return uSER


def bcolorsReset():
    rESET = '\033[0m'
    return rESET


print(bcolorsOK() + "Try your luck today and win MILLIONS!" + bcolorsReset())
quantityTips = Lotto_Funktionen_V2.quantityTips()

# Tips Auswahl + Zahlenabfrage pro Tip!
allTips = []
for i in range(0, quantityTips):
    print("Tip Nr.", i+1, ":")
    tip = Lotto_Funktionen_V2.numberInput()
    tip.sort()
    allTips.append(tip)
# Lotto-Ziehung mit Zusatzzahl
lottoNumbers = Lotto_Funktionen_V2.lottoLuckyNumbers()
extraNumber = Lotto_Funktionen_V2.extraLuckyNumber()
lottoNumbers.sort()
# Ausgabe der heutigen Lotto-Ziehung!
print(bcolorsUser() + "(Lotto-Numbers are sorted in ascending order!)\nTodays Lottery-Numbers are: ", lottoNumbers,
      "- Extra-Number: ", extraNumber, "\n" + bcolorsReset())
# Ausgabe der Tips + die Übereinstimmungen der Tips mit der heutigen Lotto-Ziehung
for i in range(0, quantityTips):
    print(i+1, "Tip =", allTips[i])
    hitCounter = Lotto_Funktionen_V2.lottoComparison(allTips[i], lottoNumbers)
    if extraNumber in allTips[i]:           # wenn eine Zahl mit der Ziehung übereinstimmt = Ergebnis in grün
        if hitCounter >= 1:                 # wenn nicht = Ergebnis in gelb
            print(bcolorsOK() + "Tip Number", i+1, "has", hitCounter, "correct prediction! + You got the extra number"
                                                                      " correct!\n" + bcolorsReset())
        else:
            print(bcolorsBackGround() + "Tip Number", i+1, "has", hitCounter,
                  "correct prediction! + You got the extra number correct!\n" + bcolorsReset())
    else:
        if hitCounter >= 1:
            print(bcolorsOK() + "Tip Number", i+1, "has", hitCounter, "correct prediction!" + bcolorsReset())
        else:
            print(bcolorsBackGround() + "Tip Number", i+1, "has", hitCounter, "correct prediction!" + bcolorsReset())
