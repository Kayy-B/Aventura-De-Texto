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

def ending1():
    win.destroy()
    sys.path.insert(0, './Pages')
    import Story1_2_1

def ending2():
    win.destroy()
    sys.path.insert(0, './Pages')
    import Story1_2_2

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
I kept thinking about it all the way home. I knew I wasnt intoxicated, or so I thought.  I have been having some problems controlling my drinking since my girlfriend broke up with me but I am pretty sure I was sober. Was it a hallucination? Was it real? Who knows. I have this weird “not giving a damn about things” and “it is what it is”  attitude since my break up and believe me, life has been going way smoother. My therapist told me that I need to face these issues head on if I want to get better and get a grip on my drinking too if I don’t want to die early. I’m like “tell me something I don’t know”. Still, that girl took my breath away. I haven’t felt this way in a very long time, this nostalgic feeling. I can’t get the thought of that girl out of my mind, it’s driving me crazy. “Who was she?”, “How did she just vanish into thin air?” . These questions messed up my mind upto the point that my anxiety peaked and I didn’t even know how I got a glass of whiskey in my hand. One thing about me, I drink to calm my nerves, to get over the many mental disorders I have been diagnosed with. At least temporarily. Alcohol helps me function and prevents me from doing “certain things” too.  
""")
text_area.configure(state ='disabled')

btn1= Button(
    win,
    text = "Option1",
    height = 5,
    width = 50,
    padx = 20,
    command=ending1,
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
    command=ending2,
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