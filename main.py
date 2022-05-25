from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Kryžiukai - Nuliukai")

mygtukas1 = ttk.Button(root, text=' ')
mygtukas1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
mygtukas1.config(command=lambda: ButtonClick(1))

mygtukas2 = ttk.Button(root, text=' ')
mygtukas2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
mygtukas2.config(command=lambda: ButtonClick(2))

mygtukas3 = ttk.Button(root, text=' ')
mygtukas3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
mygtukas3.config(command=lambda: ButtonClick(3))

mygtukas4 = ttk.Button(root, text=' ')
mygtukas4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
mygtukas4.config(command=lambda: ButtonClick(4))

mygtukas5 = ttk.Button(root, text=' ')
mygtukas5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
mygtukas5.config(command=lambda: ButtonClick(5))

mygtukas6 = ttk.Button(root, text=' ')
mygtukas6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
mygtukas6.config(command=lambda: ButtonClick(6))

mygtukas7 = ttk.Button(root, text=' ')
mygtukas7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
mygtukas7.config(command=lambda: ButtonClick(7))

mygtukas8 = ttk.Button(root, text=' ')
mygtukas8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
mygtukas8.config(command=lambda: ButtonClick(8))

mygtukas9 = ttk.Button(root, text=' ')
mygtukas9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
mygtukas9.config(command=lambda: ButtonClick(9))

playerturn = ttk.Label(root, text="   Pirmo žaidėjo eilė!  ")
playerturn.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)

playerdetails = ttk.Label(root, text="    Žaidėjas 1 is X\n\n    Žaidėjas 2 is O")
playerdetails.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)

Kartoti = ttk.Button(root, text='Pradėti iš naujo')
Kartoti.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
Kartoti.config(command=lambda: restartbutton())

a = 1
b = 0
c = 0


def restartbutton():
    global a, b, c
    a = 1
    b = 0
    c = 0
    playerturn['text'] = "   Pirmo žaidėjo eilė!   "
    mygtukas1['text'] = ' '
    mygtukas2['text'] = ' '
    mygtukas3['text'] = ' '
    mygtukas4['text'] = ' '
    mygtukas5['text'] = ' '
    mygtukas6['text'] = ' '
    mygtukas7['text'] = ' '
    mygtukas8['text'] = ' '
    mygtukas9['text'] = ' '
    mygtukas1.state(['!disabled'])
    mygtukas2.state(['!disabled'])
    mygtukas3.state(['!disabled'])
    mygtukas4.state(['!disabled'])
    mygtukas5.state(['!disabled'])
    mygtukas6.state(['!disabled'])
    mygtukas7.state(['!disabled'])
    mygtukas8.state(['!disabled'])
    mygtukas9.state(['!disabled'])


def disableButton():
    mygtukas1.state(['disabled'])
    mygtukas2.state(['disabled'])
    mygtukas3.state(['disabled'])
    mygtukas4.state(['disabled'])
    mygtukas5.state(['disabled'])
    mygtukas6.state(['disabled'])
    mygtukas7.state(['disabled'])
    mygtukas8.state(['disabled'])
    mygtukas9.state(['disabled'])


def ButtonClick(id):
    global a, b, c
    print("ID:{}".format(id))

    if id == 1 and mygtukas1['text'] == ' ' and a == 1:
        mygtukas1['text'] = "X"
        a = 0
        b += 1
    if id == 2 and mygtukas2['text'] == ' ' and a == 1:
        mygtukas2['text'] = "X"
        a = 0
        b += 1
    if id == 3 and mygtukas3['text'] == ' ' and a == 1:
        mygtukas3['text'] = "X"
        a = 0
        b += 1
    if id == 4 and mygtukas4['text'] == ' ' and a == 1:
        mygtukas4['text'] = "X"
        a = 0
        b += 1
    if id == 5 and mygtukas5['text'] == ' ' and a == 1:
        mygtukas5['text'] = "X"
        a = 0
        b += 1
    if id == 6 and mygtukas6['text'] == ' ' and a == 1:
        mygtukas6['text'] = "X"
        a = 0
        b += 1
    if id == 7 and mygtukas7['text'] == ' ' and a == 1:
        mygtukas7['text'] = "X"
        a = 0
        b += 1
    if id == 8 and mygtukas8['text'] == ' ' and a == 1:
        mygtukas8['text'] = "X"
        a = 0
        b += 1
    if id == 9 and mygtukas9['text'] == ' ' and a == 1:
        mygtukas9['text'] = "X"
        a = 0
        b += 1

    if id == 1 and mygtukas1['text'] == ' ' and a == 0:
        mygtukas1['text'] = "O"
        a = 1
        b += 1
    if id == 2 and mygtukas2['text'] == ' ' and a == 0:
        mygtukas2['text'] = "O"
        a = 1
        b += 1
    if id == 3 and mygtukas3['text'] == ' ' and a == 0:
        mygtukas3['text'] = "O"
        a = 1
        b += 1
    if id == 4 and mygtukas4['text'] == ' ' and a == 0:
        mygtukas4['text'] = "O"
        a = 1
        b += 1
    if id == 5 and mygtukas5['text'] == ' ' and a == 0:
        mygtukas5['text'] = "O"
        a = 1
        b += 1
    if id == 6 and mygtukas6['text'] == ' ' and a == 0:
        mygtukas6['text'] = "O"
        a = 1
        b += 1
    if id == 7 and mygtukas7['text'] == ' ' and a == 0:
        mygtukas7['text'] = "O"
        a = 1
        b += 1
    if id == 8 and mygtukas8['text'] == ' ' and a == 0:
        mygtukas8['text'] = "O"
        a = 1
        b += 1
    if id == 9 and mygtukas9['text'] == ' ' and a == 0:
        mygtukas9['text'] = "O"
        a = 1
        b += 1


    if (mygtukas1['text'] == 'X' and mygtukas2['text'] == 'X' and mygtukas3['text'] == 'X' or
            mygtukas4['text'] == 'X' and mygtukas5['text'] == 'X' and mygtukas6['text'] == 'X' or
            mygtukas7['text'] == 'X' and mygtukas8['text'] == 'X' and mygtukas9['text'] == 'X' or
            mygtukas1['text'] == 'X' and mygtukas4['text'] == 'X' and mygtukas7['text'] == 'X' or
            mygtukas2['text'] == 'X' and mygtukas5['text'] == 'X' and mygtukas8['text'] == 'X' or
            mygtukas3['text'] == 'X' and mygtukas6['text'] == 'X' and mygtukas9['text'] == 'X' or
            mygtukas1['text'] == 'X' and mygtukas5['text'] == 'X' and mygtukas9['text'] == 'X' or
            mygtukas3['text'] == 'X' and mygtukas5['text'] == 'X' and mygtukas7['text'] == 'X'):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Kryžiukai - Nuliukai", "Pirmas žaidėjas laimėjo! ")
    elif (mygtukas1['text'] == 'O' and mygtukas2['text'] == 'O' and mygtukas3['text'] == 'O' or
          mygtukas4['text'] == 'O' and mygtukas5['text'] == 'O' and mygtukas6['text'] == 'O' or
          mygtukas7['text'] == 'O' and mygtukas8['text'] == 'O' and mygtukas9['text'] == 'O' or
          mygtukas1['text'] == 'O' and mygtukas4['text'] == 'O' and mygtukas7['text'] == 'O' or
          mygtukas2['text'] == 'O' and mygtukas5['text'] == 'O' and mygtukas8['text'] == 'O' or
          mygtukas3['text'] == 'O' and mygtukas6['text'] == 'O' and mygtukas9['text'] == 'O' or
          mygtukas1['text'] == 'O' and mygtukas5['text'] == 'O' and mygtukas9['text'] == 'O' or
          mygtukas3['text'] == 'O' and mygtukas5['text'] == 'O' and mygtukas7['text'] == 'O'):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Kryžiukai - Nuliukai", "Antras žaidėjas laimėjo!")
    elif b == 9:
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Kryžiukai - Nuliukai", "Lygiosios.")

    if a == 1 and c == 0:
        playerturn['text'] = "   Pirmo žaidėjo eilė!   "
    elif a == 0 and c == 0:
        playerturn['text'] = "   Antro žaidėjo eilė!   "


root.mainloop()
