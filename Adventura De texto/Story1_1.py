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
win.title("Story1_1")
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
As I turned, she was not there, yes! She disappeared.  
I was in shock and screamed so loud that not even a single person came there. I went back to my kids Archana and Arnab and told them all about that. I don't know why but instead of being afraid they just laughed at me (this wasn't acceptable), but then they made me realize that I was dreaming, I was at peace now.  
Then, I got back to my room and started watching television to divert my mind. I was thirsty and called Archana to get me a glass of water, meanwhile, I heard my son watching the news and the same incident came, she was murdered by a killer. I got back to that place in a hurry and saw an investigation was going on. I stepped back and started walking on another side of the road without looking at strangers.  
I heard people around talking about the murder, and one said that it happened because the girl wasn't ready to marry the guy. The case wasn't solved as it has been two years since Archana and Arnab's father came from Boston-we were very happy and full of enjoyment and celebration. When I looked up at him and saw his face there was fear on his face, I don't know why but when I asked him, he moved to the bed and slept. After two years, we were having brunch together. I was contented but suddenly I saw Stephen was wearing the same bangle as the girl who was murdered. 
Omg! Why did this incident come to mind again, I left the dining area and went to wash my face. The bell rang and the postman came to deliver a letter - it was for my husband, I opened it and read it and the person was asking him for forty thousand dollars otherwise they'd kill him. I was exasperated with this letter thinking about what had happened to my husband and why all this was happening.  
Suddenly, my husband left home; it had been two days since he wasn't back. The bell rang and the RBI came to our house along with my Stephen, I mean, I didn't make any complaint, but then officers told us the same incident that I was familiar with, and they just told Stephen was the killer. 
I couldn't believe it and started crying and screaming and felt ill and was hospitalized. I was in dilemma to choose between Stephen or truth, I chose truth, and that's why my kids were proud of me. 
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