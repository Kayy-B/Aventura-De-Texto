from tkinter import *
from winconfig import *
import sys
sys.path.insert(0, './Pages')
win = Tk()
w = mainWindow(win)
window = Mbar(win)
w.set()
window.nav()
win.title("Index")
bgimg = PhotoImage(file = "my aventura\img2.png")

def Back():
    win.destroy()
    import menu

def story1():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story1

def story2():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story2

A = ("Gabriola", 30, "bold")

ttl = Label(win,image = bgimg).place(x=0, y=0, relwidth=1, relheight=1)
backGroundimage = Label(win, )
backGroundimage.pack()

BACK = Button(
    win,
    font = A,
    command = Back,
    height = 1,
    width = 15,
    pady = 3,
    text = "Back",
    background = "white",
    foreground = "#850101",
    ).place(x= 1300,y=0)

Story1 = Button(
    win,
    text = "Story 1",
    font = A,
    command = story1,
    bd = 5,
    justify=CENTER,
    height = 1,
    bg = "#001100",
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    ).place(x=300,y=535)

Story2 = Button(
    win,
    text = "Story 2",
    font = A,
    command = story2,
    bd = 5,
    justify=CENTER,
    height = 1,
    bg = "#000000",
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    ).place(x=1000,y=535)

win.mainloop()