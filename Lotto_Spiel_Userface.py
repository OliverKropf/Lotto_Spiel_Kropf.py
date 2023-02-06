from tkinter import *
from LottoFuktionen import Lotto_Userface_Funktionen
clickCounter = 0
userList = []


def tip_Check():
    def tipSaving():
        global clickCounter
        clickCounter = clickCounter + 1
        try:
            userList = numberInput()
            # print(userList)
            deleteInput()
            lblErrorOutput.config(text='')
            errorCount = Lotto_Userface_Funktionen.numberRangeCheck(userList)
            if errorCount == 1:
                Lotto_Userface_Funktionen.listClearing(userList)
                clickCounter = clickCounter - 1
                lblErrorOutput.config(text='Keine Doppelten Zahlen\nbei Zahleneingabe!')
            elif errorCount == 2:
                Lotto_Userface_Funktionen.listClearing(userList)
                clickCounter = clickCounter - 1
                lblErrorOutput.config(text='Ihre eingegebenen Zahlen müssen\nzwischen 1 - 45 liegen!')
            else:
                if clickCounter == tipQuantity:
                    entryAndButtonOkDisable()
                    lblLotteryOutput.config(text=Lotto_Userface_Funktionen.lottoComparison(userList))
                else:
                    lblLotteryOutput.config(text='')
                return listOutput(userList)
        except:
            deleteInput()
            clickCounter = clickCounter - 1
            lblErrorOutput.config(text='Fehler - Zahleneingabe!\nInput erwartet ganze ZAHLEN!')
    # | Funktion tip_Check |
    try:
        clickCounter = 0
        tipQuantity = int(txtTipInput.get())
        if 1 <= tipQuantity <= 4:
            clickCounter = clickCounter + 1
            tipOutputAndEntryEnable(tipQuantity)
            lblErrorOutput.config(text='')
            btnOK.config(command=tipSaving)
        else:
            lblErrorOutput.config(text='Fehler bei Tip-Eingabe\nMin. 1 Tip, Max. 4 Tips!')
    except:
        lblErrorOutput.config(text='Fehler bei Tip-Eingabe!\nEs sind nur ganze Zahlen erlaubt!')


def btn_Quit():     # Exit Button
    quitWindow = Toplevel(myWindow)
    quitWindow.geometry('380x100')
    quitWindow.title('Wollen Sie das Programm beenden?')
    btnYes = Button(quitWindow, text='JA', command=myWindow.destroy)
    btnNo = Button(quitWindow, text='NEIN', command=quitWindow.destroy)
    btnYes.place(x=107, y=50)
    btnNo.place(x=215, y=50)


def numberInput():   # Liste mit User-Zahlen
    userList.append(int(txtInput1.get()))
    userList.append(int(txtInput2.get()))
    userList.append(int(txtInput3.get()))
    userList.append(int(txtInput4.get()))
    userList.append(int(txtInput5.get()))
    userList.append(int(txtInput6.get()))
    return userList


def entryAndButtonOkDisable():   # Alle Input-Felder & OK-Button werden DISABLED, QUIT-Button wird ENABLED
    txtInput1.config(background='darkgrey', state=DISABLED)
    txtInput2.config(background='darkgrey', state=DISABLED)
    txtInput3.config(background='darkgrey', state=DISABLED)
    txtInput4.config(background='darkgrey', state=DISABLED)
    txtInput5.config(background='darkgrey', state=DISABLED)
    txtInput6.config(background='darkgrey', state=DISABLED)
    btnOK.config(background='darkgrey', state=DISABLED)
    btnQuit.config(background='white', state=NORMAL)


def tipOutputAndEntryEnable(tipQuantity):   # Nach Tip eingabe werden Input-Felder ENABLED und
    txtInput1.config(state=NORMAL, background="white")          # Label-Ausgabe: Wieviele Tips
    txtInput2.config(state=NORMAL, background="white")
    txtInput3.config(state=NORMAL, background="white")
    txtInput4.config(state=NORMAL, background="white")
    txtInput5.config(state=NORMAL, background="white")
    txtInput6.config(state=NORMAL, background="white")
    txtTipInput.config(state=DISABLED, background="darkgrey")
    if tipQuantity == 1:
        lblTipOutput.config(text='Tip 1:')
    elif tipQuantity == 2:
        lblTipOutput.config(text='Tip 1:\nTip 2:')
    elif tipQuantity == 3:
        lblTipOutput.config(text='Tip 1:\nTip 2:\nTip 3:')


def listOutput(userList):   # Ausgabe der eingegebenen Tips
    if len(userList) == 6:
        lblUserOutput1.config(text=userList)
    elif 6 < len(userList) <= 12:
        lblUserOutput2.config(text=userList[6:12])
    elif len(userList) == 18:
        lblUserOutput3.config(text=userList[12:18])
    else:
        lblUserOutput4.config(text=userList[18:24])


def deleteInput():  # Input-Felder werden ge-cleared
    txtInput1.delete(0, 'end')
    txtInput2.delete(0, 'end')
    txtInput3.delete(0, 'end')
    txtInput4.delete(0, 'end')
    txtInput5.delete(0, 'end')
    txtInput6.delete(0, 'end')


myWindow = Tk()
myWindow.title('Lotterie Kropf! Unglaubliche Gewinnchancen!!!')
myWindow.geometry('1100x400')
myWindow.minsize(width=1100, height=400)


# Festlegen des Layouts
lblHeader = Label(myWindow, justify=LEFT, font=('Elephant', 20), text='Lotterie-Spiel', foreground='darkblue')
lblHeaderText = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 14), text='Sie können bis zu 4 Tips wählen.\n'
                                                                               'Geben sie ihre Lotto-Zahlen ein:')
lblHeaderNumberField = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='Zahlenfelder 1 - 6:')
txtInput1 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
txtInput2 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
txtInput3 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
txtInput4 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
txtInput5 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
txtInput6 = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), background='darkgrey', state=DISABLED)
btnOK = Button(myWindow, text="OK", font=('Comic Sans MS', 12), command=tip_Check)
lblHeaderUserOutput = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 14), text='Wie viele Tips wollen Sie?')
txtTipInput = Entry(myWindow, justify=LEFT, width=2, font=('Comic Sans MS', 10), foreground='black')
lblTipOutput = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='Tip 1:\nTip 2:\nTip 3:\nTip 4:', foreground='darkblue')
lblUserOutput1 = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='', foreground='black')
lblUserOutput2 = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='', foreground='black')
lblUserOutput3 = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='', foreground='black')
lblUserOutput4 = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='', foreground='black')
lblErrorHeader = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 14), text='Error-Box:', foreground='darkred', relief="raised")
lblErrorOutput = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 11), text='', width=30, height=3, foreground='red', relief="sunken", borderwidth=3)
btnQuit = Button(myWindow, text="BEENDEN", font=('Comic Sans MS', 12), background='darkgrey', command=btn_Quit, state=DISABLED)
lblLotteryOutputHeader = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 14), text='Lotto-Ziehung:', foreground='darkgreen', relief="raised")
lblLotteryOutput = Label(myWindow, justify=LEFT, font=('Comic Sans MS', 12), text='', foreground='green', width=35, height=4, relief="sunken", borderwidth=3)


# Positionierung
lblHeader.place(x=50, y=5)
lblHeaderText.place(x=50, y=50)
lblHeaderNumberField.place(x=400, y=45)
txtInput1.place(x=400, y=80)
txtInput2.place(x=440, y=80)
txtInput3.place(x=480, y=80)
txtInput4.place(x=520, y=80)
txtInput5.place(x=560, y=80)
txtInput6.place(x=600, y=80)
btnOK.place(x=700, y=75)
lblHeaderUserOutput.place(x=50, y=115)
txtTipInput.place(x=300, y=120)
lblTipOutput.place(x=340, y=115)
lblUserOutput1.place(x=400, y=115)
lblUserOutput2.place(x=400, y=138)
lblUserOutput3.place(x=400, y=161)
lblUserOutput4.place(x=400, y=184)
lblErrorHeader.place(x=50, y=220)
lblErrorOutput.place(x=50, y=250)
btnQuit.place(x=700, y=130)
lblLotteryOutputHeader.place(x=650, y=220)
lblLotteryOutput.place(x=650, y=250)


myWindow.mainloop()
