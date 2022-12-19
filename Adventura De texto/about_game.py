import tkinter as tk
import tkinter.scrolledtext as st
import sys
sys.path.insert(0, './Pages')

# Creating tkinter window
win = tk.Tk()
win.title("About Game")
win.geometry("1280x720")

# Title Label
tk.Label(win,
         text = "About Game",
         font = ("Times New Roman", 30),
         background = 'green',
         foreground = "white").pack()

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
It’s adventure time !
The goal is to survive in the story which you will create…
The rule is simple,
Make the correct choices 
And boom ! 
There you become your own story teller.

With the ups and downs of thrill 
With the horror jump scares 
And with your rom-com fantasies,
The story keeps getting catchy at every step with plot twists at every move.

Find out
If u can cleverly pick the correct plots and make your way till the end 
Or get stuck in a clueless plot, where you are left with no choice !
But to choose :)

So c’mon 
What are you waiting for ?
It’s time to be a hero !
Happy text adventuring !
""")
text_area.configure(state ='disabled')

def back():
    win.destroy()
    import menu
CONTINUE = tk.Button(
    win,
    text = "Back to Home",
    height = 2,
    width = 50,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    command=back
    ).pack()

DRKMD = tk.Button(win,
               height = 2,
               width = 15,
               pady = 3,
               text = "Toggle Darkmode",
               background = "white",
               foreground = "#850101",
               command = DarkMode,
               ).place(x = 1100, y = 0)

win.mainloop()