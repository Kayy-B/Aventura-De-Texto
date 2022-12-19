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
God, this girl is driving me crazy. It’s been a week of me visiting the station at the same time and I haven’t even caught a glimpse of that girl. Bummer. I had almost given up and was waiting for the train and suddenly I heard a voice that gave me goosebumps. It was that girl. I didn’t know how to react and I was anxious as hell. I tried using a breathing technique told by my therapist to cope with the symptoms. The girl stood next to me and was waiting for the train too. I literally stared at her through my peripheral vision, It was an awkward situation. We got in the train and she sat opposite to me , texting somebody and just looking gorgeous. A mere look at her made me blush hard. I wanted to talk to her so bad but holy shit I couldn’t muster up the courage. I hate being this introverted sometimes, I mean It has its perks but still being an introvert with a bad mental health Is hard. So I was just getting side glimpses of her in that empty train, waiting for my chance to strike a conversation. Just as I was about to do so, I heard her say “Dude are you okay?, You’re sweating so hard in peak winter”. I looked at her to give a reply and her face made my heart skip a beat and I go like “Yeah yeah yeah, I’m okay, I’m just coming from the gym that’s all”. Who’s gonna tell her that it was her that made me sweat so hard. Just like that a conversation began and we chatted for like half an hour and oh my god I didn’t want that moment to end.  But sadly my station came and that meant that the good time had to come to an end. I stood up and just when the train was about to stop , a really bad jerk came as if the emergency brakes had been applied and I fell forward. I got up and looked back at the girl to check if she was okay and I was shook to my core. It happened again, the girl had vanished without a trace. I just stood there and smiled. Days passed and somehow with the help of my therapist I had just accepted everything that happened. I am getting a grip on my drinking too and getting my life back on track. Maybe it was a hallucination, maybe it was all real and the supernatural is real too but I still have my “who gives a damn” attitude and it’s true that “it is what it is". 
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