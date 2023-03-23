import tkinter as tk
from tkinter import*




game = tk.Tk()
game.resizable(False, False)
game.title("Tic tac toe")
game.iconbitmap("test.ico")

menubar = Menu(game)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Jouer contre un autre joueur")
menu1.add_command(label="Jouer contre l'ordinateur")
menu1.add_command(label="Niveau de l'ordinateur")
menu1.add_command(label="Recommencer")
menu1.add_separator()
menu1.add_command(label="Quitter", command=game.quit)
menubar.add_cascade(label="Options", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Score")
menu2.add_command(label="Historique")
menu2.add_command(label="Tic Tac Toe Premium à seulement 24€99 par mois")
menubar.add_cascade(label="Historique", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Règles du jeu")
menubar.add_cascade(label="Aide", menu=menu3)

game.config(menu=menubar)
tk.Label(game, text="Tic Tac Toe", font=('Ariel', 25)).pack()
status_label = tk.Label(game, text="Au tour de X", font=('Ariel', 15), bg='grey', fg='ivory')
status_label.pack(fill=tk.X)

def play_again():
  print("here we go!")
  status_label.configure(text="Au tour du joueur X", bg='blue', fg='ivory')
  global player
  global checklist
  global XO_list
  player = 'X'
  
  button0.configure(state= NORMAL, text="", bg='grey')
  button1.configure(state= NORMAL, text="", bg='grey')
  button2.configure(state= NORMAL, text="", bg='grey')
  button3.configure(state= NORMAL, text="", bg='grey')
  button4.configure(state= NORMAL, text="", bg='grey')
  button5.configure(state= NORMAL, text="", bg='grey')
  button6.configure(state= NORMAL, text="", bg='grey')
  button7.configure(state= NORMAL, text="", bg='grey')
  button8.configure(state= NORMAL, text="", bg='grey')
  checklist = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
  XO_list = []
  buttonReset.pack_forget()
buttonReset = tk.Button(game, text='Rejouer ?', font=('Ariel', 15),bg='yellow', width=8, height=4, command=play_again)
  

player = "X"
computer = 0
global pos
X_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
O_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
XO_list = []
AI_list = []
checklist = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
checklist2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

game.geometry("500x500")

condition = False
condition2 = False
def check_win():
 if condition==True:
    print("game over!")
 else:
    print("continue")

def check_win2():
 if condition2==True:
   print("game over!")
 else:
   print("continue")
   
def test_condition():
 if (checklist[0] == checklist[1]  == checklist[2] == "X" or
     checklist[3] == checklist[4]  == checklist[5] == "X"  or
     checklist[6] == checklist[7]  == checklist[8] == "X"  or
     checklist[0] == checklist[3]  == checklist[6] == "X"  or
     checklist[1] == checklist[4]  == checklist[7] == "X"  or
     checklist[2] == checklist[5]  == checklist[8] == "X"  or
     checklist[0] == checklist[4]  == checklist[8] == "X"  or
     checklist[2] == checklist[4]  == checklist[6] == "X"):
      condition==True
      print ("game over, X a gagné!")
      status_label.configure(text="X a gagné !", bg='blue')
      reset()
 elif (checklist[0] == checklist[1]  == checklist[2] == "O" or
     checklist[3] == checklist[4]  == checklist[5] == "O"  or
     checklist[6] == checklist[7]  == checklist[8] == "O"  or
     checklist[0] == checklist[3]  == checklist[6] == "O"  or
     checklist[1] == checklist[4]  == checklist[7] == "O"  or
     checklist[2] == checklist[5]  == checklist[8] == "O"  or
     checklist[0] == checklist[4]  == checklist[8] == "O"  or
     checklist[2] == checklist[4]  == checklist[6] == "O"):
      condition==True
      print ("game over, O a gagné!")
      status_label.configure(text="O a gagné!", bg='red')
      reset()
 elif len(XO_list)==9:
     print("égalité!")
     status_label.configure(text="Egalité !", bg='green')
     reset()

   
 if (checklist2[0] == checklist2[1]  == checklist2[2] == 1 or
     checklist2[3] == checklist2[4]  == checklist2[5] == 1 or
     checklist2[6] == checklist2[7]  == checklist2[8] == 1 or
     checklist2[0] == checklist2[3]  == checklist2[6] == 1 or
     checklist2[1] == checklist2[4]  == checklist2[7] == 1 or
     checklist2[2] == checklist2[5]  == checklist2[8] == 1 or
     checklist2[0] == checklist2[4]  == checklist2[8] == 1 or
     checklist2[2] == checklist2[4]  == checklist2[6] == 1 ):
      condition2==True
      
    
     
def symbol_player():
 global player
 
 if player == 'X':
  
  XO_list.append('X')
  print(XO_list)
  print(checklist)
  print(checklist2)
  player = "O"
  status_label.configure(text="Au tour du joueur O", bg='red', fg='ivory')
 elif player == "O":
 
  XO_list.append('O')
  print(XO_list)
  print(checklist)
  player = "X"
  status_label.configure(text="Au tour du joueur X", bg='blue', fg='ivory')
check_win()
check_win2()


def click0():
 print("0")
 button0.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[0] = player
 checklist2[0] = 1
 
 

def click1():
 print("1")
 button1.configure(bg="ivory", text = player,fg = 'black',state= DISABLED)
 checklist[1] = player
 checklist2[1] = 1
 


def click2():
 print("2")
 button2.configure(bg="ivory", text = player,  fg = 'black',state= DISABLED)
 checklist[2] = player
 checklist2[2] = 1
 

def click3():
 print("3")
 button3.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[3] = player
 checklist2[3] = 1
 

def click4():
 print("4")
 button4.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[4] = player
 checklist2[4] = 1
 

def click5():
 print("5")
 button5.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[5] = player
 checklist2[5] = 1
 

def click6():
 print("6")
 button6.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[6] = player
 checklist2[6] = 1
 

def click7():
 print("7")
 button7.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[7] = player
 checklist2[7] = 1
 

def click8():
 print("8")
 button8.configure(bg="ivory", text = player, fg = 'black',state= DISABLED)
 checklist[8] = player
 checklist2[8] = 1
 
 
def set(self):
 print('ok')
 


button0 = tk.Button(game, text ="", bg='grey', width=10, height=5,  command=lambda:[click0(),symbol_player(), test_condition()])
button0.place(x=100, y=100)

button1 = tk.Button(game, text ="",bg='grey', width=10, height=5,command=lambda:[click1(),symbol_player(), test_condition()])
button1.place(x=200, y=100)

button2 = tk.Button(game, text ="",bg='grey', width=10, height=5,  command=lambda:[click2(),symbol_player(), test_condition()])
button2.place(x=300, y=100)

button3 = tk.Button(game, text ="",bg='grey', width=10, height=5, command=lambda:[click3(),symbol_player(), test_condition()])
button3.place(x=100, y=200)

button4 = tk.Button(game, text ="",bg='grey', width=10, height=5,command=lambda:[click4(),symbol_player(), test_condition()])
button4.place(x=200, y=200)

button5 = tk.Button(game, text ="",bg='grey', width=10, height=5, command=lambda:[click5(),symbol_player(), test_condition()])
button5.place(x=300, y=200)

button6 = tk.Button(game, text ="",bg='grey', width=10, height=5, command=lambda:[click6(),symbol_player(), test_condition()])
button6.place(x=100, y=300)

button7 = tk.Button(game, text ="",bg='grey', width=10, height=5, command=lambda:[click7(),symbol_player(), test_condition()])
button7.place(x=200, y=300)

button8 = tk.Button(game, text ="",bg='grey', width=10, height=5, command=lambda:[click8(),symbol_player(), test_condition()])
button8.place(x=300, y=300)



def reset():
  
  global buttonReset
  print("Jouer encore ?")
  buttonReset.pack()
  buttonReset.place(x=200, y=400)
  
 
 
game.mainloop()