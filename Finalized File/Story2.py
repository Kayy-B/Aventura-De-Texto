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
win.title("Story2")
#-----------------------------------------------------# 
"DEFINITIONS"

A = ("Gabriola", 40)
 
B = ("News Gothic MT Regular", 20)

def Back():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import index

def opn1():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story2_1

def opn2():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story2_2

def opn3():
    win.destroy()
    sys.path.insert(0,'./Pages')
    import Story2_3

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
"""It was hell of a long week and I finally can go home and get some shut eye. At least,
it was supposed to be.\n
    "Hey, listen," my boss called out as he approached me.
I let out a sigh as I turned to look at him, a polite smile plastered on my face. "Yes, sir?"\n
    "I know it's late but can you complete this report on this financial year?" he said while
handing me a pendrive, "I could've done it myself but I already have prior commitments and
you're the only guy who I could trust with this."\n
    "No problem, sir, I understand. I will get the report ready," I responded politely.\n
    "Really? Thanks pal, I knew I could trust you!" He exclaimed as he patted my arm.
He then left, putting his patterned grey suit over his shoulder.\n
    I maintained my smile till his footsteps faded then I let out a groan.\n
    "'Prior commitments'," I scoffed as I stared at the pendrive on my palm, "Well, I guess I can
kiss my long awaited weekends good-bye."\n
    I began trudging my way to the metro. It was pretty full as usual, and it would be whishful
thinking to expect a decent seat. Apart from the usual rush hour the nearing of the weekends
vitalized even those who knew not of sleep.\n
    I took the cramped metro to my destination and pushed my way to the exit. I made my way
past the bustling streets to my small apartment, located at a quieter, back-end side of the city.\n
    The apartment itself was nothing special. Many would have confuesed it for a shutdown
storage center. However, the biggest advantage was that the rent was so cheap that even a salaryman like me could afford it.\n
    The door let out a creak and stopped midway as I opened the door. With a sigh, I squeezed
through the half opened door, making a mental note to myself to re-lubricate the hinges. The wood underneath
creaked as I made my way to the living-room to work.\n
    I was soo absorbed in my work, trying to complete the report that I shouldn't even be made to do, I was jolted out of my thoughts when I head someone knocking on my front door.\n
    "Yes? Who is it?" I asked as I went to the door. However, I was responded with silence.\n
    Another major annoyance. The bell worked fine and well...Only for the first few days, that is. And if I had a penny for every time I called the maintanance to fix the damn bell, I wouldn't
even be working overtime right now.\n
    I did not have a peep hole on the door, either. This made it easy for those "funny guys" to pull pranks on me.\n
    As I was debating whether to open the door, the knocking on the door again started, but this
time it was louder than before. Being at my wits
end, I decided to...""")
text_area.configure(state ='disabled')

btn1= Button(
    win,
    text = "Option 1",
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
    text = "Option 2",
    height = 5,
    width = 50,
    padx = 20,
    command=opn2,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).place(x=575,y=648)

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

DRKMD = Button(win,
               height = 2,
               width = 15,
               pady = 3,
               text = "Toggle Darkmode",
               background = "white",
               foreground = "#850101",
               command = DarkMode,
               ).place(x = 1100, y = 0)

BACK = tk.Button(
    win,
    text = "Back",
    font = B,
    command = Back,
    height = 2,
    width = 5,
    padx = 40,
    fg = "#14425A",
    background = "#A5A5A5",
    ).place(x = 1300, y = 0)

win.mainloop()