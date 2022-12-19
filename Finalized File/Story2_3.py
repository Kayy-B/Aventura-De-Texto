import tkinter as tk
import tkinter.scrolledtext as st
from winconfig import *
import sys
sys.path.insert(0, '/Hackathon Project')
win = tk.Tk()
w = story2Window(win)
window = Mbar(win)
w.set()
window.nav()
win.title("Story2_3")
#-----------------------------------------------------# 
"DEFINITIONS"

A = ("Gabriola", 40)

B = ("News Gothic MT Regular", 20)
  
def Back():
    win.destroy()
    sys.path.insert(0, './Pages')
    import Story2

def index():
    win.destroy()
    sys.path.insert(0, './Pages')
    import index

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
#-----------------------------------------------------#
background = Label(
    win,
    font = A,
    justify = CENTER,
    foreground = "#000000",
    background = "#ffffff",
    padx = 355,
).place(x = 0, y = 70)



# Title Label
tk.Label(win,
         text = "Story 2",
         font = ("Times New Roman", 30),
         background = 'light blue',
         foreground = "white").pack()

# Creating scrolled text area
# widget with Read only by
# disabling the state
text_area = st.ScrolledText(win,
                            height = 16,
                            font = ("Times New Roman",20))

text_area.pack(pady = 10, padx = 10)

# Inserting Text which is read only
text_area.insert(tk.INSERT,
"""

I hate it while my brother Charlie has to head away. My mother and father continuously try and provide an explanation for to me how unwell he's. That I am fortunate for having a mind wherein all of the chemical substances go with the drift nicely to their locations like undammed rivers. When I whinge approximately how bored I am with out a bit brother to play with, they are attempting to make me experience horrific with the aid of using mentioning that his boredom probably some distance surpasses mine, thinking about his confine to a darkish room in an institution. I usually beg for them to present him one remaining chance. Of course, they did at first. Charlie has been returned domestic numerous times, every shorter in period than the remaining. Every time with out fail, all of it begins offevolved again. The neighbourhood cats with gouged out eyes displaying up in his toy chest, my dad’s razors determined dropped at the toddler slide withinside the park throughout the street, mom’s nutrients changed with the aid of using bits of dishwasher tablets. My mother and father are hesitant now, using “remaining chances” sparingly. They say his sickness makes him charming, makes it smooth for him to faux normalcy, and to trick the docs who take care of him into questioning he is prepared for rehabilitation. That I will simply ought to positioned up with my boredom if it way staying secure from him. I hate it while Charlie has to head away. It makes me ought to fake to be right till he's returned.

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