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
win.title("Story2_1")
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
"""As I turned, she was not there, yes! She disappeared. 
I was in shock and screamed so loud that not even a single person came there. I went back to my kids Archana and Arnab and told them all about that. I don't know why but instead of being afraid they just laughed at me (this wasn't acceptable), but then they made me realize that I was dreaming, I was at peace now. 
Then, I got back to my room and started watching television to divert my mind. I was thirsty and called Archana to get me a glass of water, meanwhile, I heard my son watching the news and the same incident came, she was murdered by a killer. I got back to that place in a hurry and saw an investigation was going on I stepped back and started walking on another side of the road without looking at strangers. 
I heard people around talking about the murder, and one said that it happened because the girl wasn't ready to marry the guy. The case wasn't solved as it has been two years since Archana and Arnab's father came from Boston-we were very happy and full of enjoyment and celebration. When I looked up at him and saw his face there was fear on his face, I don't know why but when I asked him he moved to the bed and slept. After two years, we were having brunch together I was contented but suddenly I saw Stephen was wearing the same bangle as that of the girl who was murdered.
Omg! why this incident came to mind again, I left the dining area and went to wash my face. The bell rang and the postman came to deliver a letter - it was for my husband, I opened it and read it and the person was asking him for forty thousand dollars otherwise they'd kill him. I was exasperated with this letter thinking about what had happened to my husband and why all this was happening. 
Suddenly, my husband left home; it had been two days since he wasn't back. The bell rang and the RBI came to our house along with my Stephen, I mean, I didn't make any complaint, but then officers told us the same incident that I was familiar with and they just told Stephen was the killer.
I couldn't believe it and started crying and screaming and felt ill and was hospitalized. I was in dilemma to choose between Stephen or truth, 
I chose truth, and that's why my kids were proud of me.
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