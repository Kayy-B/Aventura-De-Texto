from tkinter import *
from winconfig import *
import sys
sys.path.insert(0, './Pages')
root = Tk()
w = mainWindow(root)
window = Mbar(root)
w.set()
window.nav()
#-----------------------------------------------------#
"DEFINITIONS"

bgimg = PhotoImage(file = "Adi aventura\img1.png")
    
def Play():
    root.destroy()
    sys.path.insert(0, './Pages')
    import intro
    
def Quit():
    root.destroy()

A = ("Gabriola", 30, "bold")

B = ("News Gothic MT Regular", 20)

#-----------------------------------------------------#
"Background Image + Title"

ttl = Label(root,image = bgimg).place(x=0, y=0, relwidth=1, relheight=1)

backgroundimage = Label(root, )

#------------------------------------------------------#

QUIT = Button(
    root,
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
    root,
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

root.mainloop()
