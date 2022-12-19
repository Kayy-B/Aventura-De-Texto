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
win.title("Story2_2")
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
As I was debating whether to open the door, the knocking on the door again started, but this 
time it was louder than before. Being at my wits end, I decided to open the door and give the 
stranger a piece of my mind.I immediately opened the door, ready to yell however, I found myself staring at a patterned, 
velvet package. Taking a closer look at it, it had my name and address on it, however I had no 
recollection of ordering anything of such sort.
After surveying the area to see whether anybody has left it here, I took the package 
and closed the door. I placed the package on the table and thought about what I would do with it. 
It I did not order it, and neither did anybody I know would gift me something that looked 
expensive - and without their return address, no less.
However, it had my name and address, all spelled correctly.
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