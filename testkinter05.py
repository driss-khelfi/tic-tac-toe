import tkinter
import random

#Paramètres de l'application
case=tkinter.Tk()
case.title("Tic-tac-toe")
case.geometry("400x400")


def click0(): 
    button0.configure(bg="red")
    color()
def click1(): 
    button1.configure(bg="red")
    color()
def click2(): 
    button2.configure(bg="red")
    color()
def click3(): 
    button3.configure(bg="red")
    color()
def click4(): 
    button4.configure(bg="red")
    color()
def click5(): 
    button5.configure(bg="red")
    color()
def click6(): 
    button6.configure(bg="red")
    color()
def click7(): 
    button7.configure(bg="red")
    color()
def click8(): 
    button8.configure(bg="red")
    color()

def color():
   print("test")
        


button0=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click0)
button0.grid(row=1,column=1)

button1=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click1)
button1.grid(row=1,column=2)

button2=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click2)
button2.grid(row=1,column=3)

button3=tkinter.Button(case, width = 4, height=4, borderwidth=2,bg='ivory',command= click3)
button3.grid(row=2,column=1)

button4=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click4)
button4.grid(row=2,column=2)

button5=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click5)
button5.grid(row=2,column=3)

button6=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click6)
button6.grid(row=3,column=1)

button7=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click7)
button7.grid(row=3,column=2)


button8=tkinter.Button(case, width = 4, height=4,borderwidth=2, bg='ivory',command= click8)
button8.grid(row=3,column=3)

case.mainloop()