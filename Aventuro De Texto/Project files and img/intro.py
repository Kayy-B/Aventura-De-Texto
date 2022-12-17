from tkinter import *
from winconfig import *
import sys
sys.path.insert(0, '/Hackathon Project')
import tkinter as tk
root = tk.Tk()
w = secondWindow(root)
window = Mbar(root)
w.set()
window.nav()
#-----------------------------------------------------#
"DEFINITIONS"

A = ("Gabriola", 40)

B = ("News Gothic MT Regular", 20)

def Back():
    root.destroy()
    import menu

def Enter():
    inputValue=text.get("1.0","end-1c")
    print(inputValue)
#-----------------------------------------------------#
"TEXT"
background = Label(
    root,
    text=
    '''
Greetings Traveller!
I am Narr Adorr. A humble librarian at the
Perlside Central Library, here at Perlside Point.

Before we continue, please tell me your name:\n\n\n\n\n
    ''',
    font = A,
    justify = CENTER,
    foreground = "#000000",
    background = "#ffffff",
    padx = 355,
).place(x = 0, y = 70)

text= Text(root,
           width= 50,
           height= 0,
           pady = 10,
           padx = 10,
           background= "#FFFFFF",
           foreground="#14425A",
           font= B,
           borderwidth = 5,
           relief = RIDGE)

text.insert(INSERT, "Your Name Here")

text.place(x = 300, y = 490)

#------------------------------------------------------#
"BUTTONS"

BACK = Button(
    root,
    text = "Back",
    font = B,
    command = Back,
    height = 2,
    width = 5,
    padx = 40,
    fg = "#14425A",
    background = "#A5A5A5",
    ).place(x = 1100, y = 10)

ENTER = Button(
    root,
    text = "Enter",
    font = B,
    command = Enter,
    height = 4,
    width = 50,
    fg = "#14425A",
    activebackground = "#14425A",
    activeforeground = "#ffffff"
    ).place(x = 315, y = 590)

root.mainloop()
