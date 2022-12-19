from tkinter import *
import tkinter.scrolledtext as st
import sys
sys.path.insert(0, '/Hackathon Project/Pages')
from winconfig import *
import tkinter as tk
win = tk.Tk()
w = story1Window(win)
window = Mbar(win)
w.set()
window.nav()
win.title("Story1")

#------------------------------------------------------#

#Darkmode
switch = True
def DarkMode():
    global switch
    if switch == True:
        text_area.config(background = "#333333", foreground = "white")
        win.config(background = "#333333")
        switch = False
    elif switch == False:
        text_area.config(background = "white", foreground = "#333333")
        win.config(background = "white")
        switch = True

def Back():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import index

def opn1():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story1_1
def opn2():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story1_2
def opn3():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story1_3

# Title Label
tk.Label(win,
         text = "Chapter 1",
         font = ("Times New Roman", 20),
         width = 50,
         background = '#850101',
         foreground = "white").pack()

text_area = st.ScrolledText(win,
                            height = 16,
                            font = ("Times New Roman",20),
                            highlightthickness=0)

text_area.pack(pady = 10, padx = 50)

text_area.insert(INSERT,
"""Was that a dream or was that all true, I never felt this way it was like I was in a parallel universe.\n

Let me start from the beginning, it was 6 pm and a rainy weather ya I know it sounds romantic but
trusty it was nothing like that till she arrived... I was returning from my gym waiting for the rain to
slow down suddenly I heard a voice it was soft and just made me wonder what she looked like, I
turned around to look, but I saw no one just a voice. she sounded a little tensed in her sweet voice 
she said-"stop being so rude I've been through a lot lately I don't need more of it, it made me 
wonder what so wrong? Well none of my business. The volce grew louder, and she arrived I was 
mesmerized looking at her, eyes so bright, face so calm Ishe had a hint of shyness in her smile,I 
suddenly realized I was staring her face so seriously that she might think I am a stalker so I quickly 
turned around, but the look of her face never disappeared like it was all in my head locked in forever 
the next moment the voice stopped as I turned she was not there...
""")
text_area.configure(state ='disabled')

btn1= Button(
    win,
    text = "Option1",
    height = 5,
    width = 50,
    padx = 20,
    command=opn1,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).pack(side = LEFT)

btn2 = Button(
    win,
    text = "Option2",
    height = 5,
    width = 50,
    padx = 20,
    command=opn2,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).place(x=575,y=642)

btn3 = Button(
    win,
    text = "Option 3",
    height = 5,
    width = 50,
    padx = 20,
    command=opn3,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).pack(side = RIGHT)

back = Button(
    win,
    text = "Back",
    height = 1,
    width = 15,
    padx = 20,
    command = Back,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).place(x = 1350, y = 0)

#Darkmode Button

DRKMD = Button(win,
               height = 2,
               width = 15,
               pady = 3,
               text = "Toggle Darkmode",
               background = "white",
               foreground = "#850101",
               command = DarkMode,
               ).place(x = 1100, y = 0)

win.mainloop()