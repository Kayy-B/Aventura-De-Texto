from tkinter import *
from winconfig import *
import sys
sys.path.insert(0, './Pages')
root = Tk()
w = mainWindow(root)
window = Mbar(root)
w.set()
window.nav()

bgimg = PhotoImage(file = "Adi aventura\img1.png")

def story1():
    root.destroy()
    sys.path.insert(0,'./Pages')
#    import Story1

def story2():
    root.destroy()
    sys.path.insert(0,'./Pages')
    import Story2

A = ("Gabriola", 30, "bold")

ttl = Label(root,image = bgimg).place(x=0, y=0, relwidth=1, relheight=1)

backGroundimage = Label(root, )
#backGroundimage.pack()

Story1 = Button(
    root,
    text = "Story 1 ka text",
    font = A,
    command = story1,
    bd = 5,
    justify=CENTER,
    height = 1,
    bg = "#001100",
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    )
Story1.place(x=250,y=450)

Story2 = Button(
    root,
    text = "Story 2 ka text",
    font = A,
    command = story2,
    bd = 5,
    justify=CENTER,
    height = 1,
    bg = "#000000",
    fg = "#945850",
    activebackground = "#945850",
    activeforeground = "#ffffff"
    )
Story2.place(x=800,y=450)

root.mainloop()