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
win.title("Story1_2")
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
    sys.path.insert(0, './Pages')
    import Story1

def index():
    win.destroy()
    sys.path.insert(0, './Pages')
    import index


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
"""
For the next few days I kept hearing the girls voice in my head on loop. She was the main focus of my dreams for some reason. I couldnt stop thinking about her. I never saw her again on the station. It was as if she was a ghost. Although I couldn’t care less about anything that’s not important to me but this time it was different, I did care about this. A week passed and I just thought “it is what it is” and was just walking towards the station when I passed by a newspaper vendor and a got a glimpse of a newspaper that stopped me in my track. I took two steps back and looked at the newspaper , it was a week old and there she was on the front page. I could never confuse that face with anyone else’s. I was just staring at the picture and when my eyes went on the headline that said “ Young girl took her own life by jumping in front of a train because of depression”. Something triggered inside of me at that moment and the next thing I felt was a tear running down my cheek.  I was sad. Its not like I knew the girl or something but still I was sad. The fact that troubled me the most wasn’t that I saw a ghost and lived to tell the tale but was that people don’t care about mental health much, It’s sort of a foreign concept for most of them which leads to high suicide rates. It wasn’t the first time I had heard of something like this obviously. I guess its just how the world is . But that is not enough reason to stop talking about these things right. Oh am just in case if I failed to mention this above, I am a psychiatrist.
""")
text_area.configure(state ='disabled')

btn1= Button(
    win,
    text = "Back to index",
    height = 5,
    width = 50,
    padx = 20,
    command=index,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).pack(side = LEFT)

btn2 = Button(
    win,
    text = "Back to 1st page",
    height = 5,
    width = 50,
    padx = 20,
    command=Back,
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