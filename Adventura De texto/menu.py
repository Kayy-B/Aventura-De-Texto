from tkinter import *
from winconfig import *
import sys
sys.path.insert(0, './Pages')
win = Tk()
w = mainWindow(win)
window = Mbar(win)
w.set()
window.nav()
win.title("Menu")
#-----------------------------------------------------#
"DEFINITIONS"

bgimg = PhotoImage(file = "Project files and img\img2.png")
    
def Play():
    win.destroy()
    sys.path.insert(0, './Pages')
    import index
    
def Quit():
    win.destroy()

A = ("Gabriola", 30, "bold")

B = ("News Gothic MT Regular", 20)

#-----------------------------------------------------#
"Background Image + Title"

ttl = Label(win,
            image = bgimg).place(x=0, y=0, relwidth=1, relheight=1)

backgroundimage = Label(win, )

#------------------------------------------------------#

QUIT = Button(
    win,
    text = "QUIT",
    font = B,
    command = Quit,
    height = 3,
    width = 10,
    padx = 50,
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    ).pack(pady = 30, side = BOTTOM)

PLAY = Button(
    win,
    text = "PLAY",
    font = B,
    command = Play,
    height = 3,
    width = 10,
    padx = 50,
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    ).pack(pady = 5, side = BOTTOM)

win.mainloop()
