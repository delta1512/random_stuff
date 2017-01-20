import sys
import _tkinter
import tkinter
from tkinter import *

master = Tk()
master.geometry('950x450')

global spiderprice
spiderprice = 1
global cookieprice
cookieprice = 2
global jamprice
jamprice = 3
global muffinprice
muffinprice = 4
global suma
suma = 0
global tmpspider
tmpspider = 0
global tmpcookie
tmpcookie = 0
global tmpjam
tmpjam = 0
global tmpmuffin
tmpmuffin = 0
global transno
transno = 0
transactions = open('transactions.txt', 'w')
transactions.write('\n' + 'Transaction history:')
transactions.close()

def adder(pricea):
    global suma
    suma = pricea + suma
    total.delete(0, END)
    total.insert(END, 'Total: ' + str(suma))
    return
def spidercheck(price):
    itemlist.insert(END, 'Spider $' + str(price))
    adder(price)
    global tmpspider
    tmpspider = tmpspider + 1
    return
def cookiecheck(price):
    itemlist.insert(END, 'Cookie $' + str(price))
    adder(price)
    global tmpcookie
    tmpcookie = tmpcookie + 1
    return
def jamcheck(price):
    itemlist.insert(END, 'Jam Drop $' + str(price))
    adder(price)
    global tmpjam
    tmpjam = tmpjam + 1
    return
def muffincheck(price):
    itemlist.insert(END, 'Muffin $' + str(price))
    adder(price)
    global tmpmuffin
    tmpmuffin = tmpmuffin + 1
    return
def cleara(option):
    if option == 1:
        change.delete(0, END)
    itemlist.delete(0, END)
    global suma
    suma = 0
    global tmpspider
    tmpspider = 0
    global tmpcookie
    tmpcookie = 0
    global tmpjam
    tmpjam = 0
    global tmpmuffin
    tmpmuffin = 0
    total.delete(0, END)
    total.insert(END, 'Total: ')
    return
def transaction():
    value = cashin.get()
    outval = int(value) - suma
    change.insert(END, outval)
    global transno
    transno = transno + 1
    content = str(transno) + '. Spider Qty: ' + str(tmpspider) + ', Cookie Qty: ' + str(tmpcookie) + ', Jam Qty: ' + str(tmpjam) + ', Muffin Qty: ' + str(tmpmuffin) + ', Total: ' + str(suma) + ', Cash in: ' + str(value) + ', Change: ' + str(outval)
    transactions = open('transactions.txt', 'a')
    transactions.write('\n' + str(content))
    transactions.close()
    cleara(0)
    return

spider = Button(master, text='Spider (Price_Here)', width=20, command=lambda: spidercheck(spiderprice)).grid(row=0, column=0)
cookie = Button(master, text='Cookie (Price_Here)', width=20, command=lambda: cookiecheck(cookieprice)).grid(row=0, column=1)
jam = Button(master, text='Jam Drops (Price_Here)', width=20, command=lambda: jamcheck(jamprice)).grid(row=1, column=0)
muffin = Button(master, text='Muffin (Price_Here)', width=20, command=lambda: muffincheck(muffinprice)).grid(row=1, column=1)

global itemlist
itemlist = Listbox(master, height=20)
itemlist.grid(row=4, column=0)
global cashin
cashin = Entry(master, width=20)
cashin.grid(row=1, column=3)
cashin.focus_set()
global total
total = Listbox(master, height=1)
total.grid(row=4, column=1, sticky=S)
total.insert(END, 'Total: ')
global change
change = Listbox(master, height=1)
change.grid(row=1, column=4)
listtitle = Label(master, text='Transaction contents:').grid(row=3, column=0)
clear = Button(master, text='Clear all', width=20, command=lambda: cleara(1)).grid(row=1, column=2)
endtrans = Button(master, text='Finalise Transaction', width=20, command=lambda: transaction()).grid(row=0, column=2)
entrytitle = Label(master, text='Cash Received').grid(row=0, column=3)
changetitle = Label(master, text='Change').grid(row=0, column=4)

mainloop()
