import tkinter as tk
import tkinter.scrolledtext as st
import sys
sys.path.insert(0, './Pages')

# Creating tkinter window
win = tk.Tk()
win.title("About Team")
win.geometry("1280x720")

# Title Label
tk.Label(win,
         text = "About Us",
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
Hola! People welcome to our text adventure ,
basicaly we are Interactive fiction, in which players use text commands to control characters and influence the environment.Works in this form can be understood as literary narratives, either in the form of interactive narratives or interactive narrations. These works can also be understood as a form of video game,either in the form of an adventure game or role-playing game.In common usage, the term refers to text adventures, a type of adventure game where the entire interface can be "text-only",however, graphical text adventures still fall under the text adventure category if the mainway to interact with the game is by typing text.
                                                CREATORS
                1.ADITYA MISHRA
                2.VIDIT KULSHRESTHA
                3.MUKTANSH SAXENA
                4.KANIKA BHATT
                5.VAIBHAV MALHOTRA
                6.NISHA TYAGI
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
# Making the text read only
win.mainloop()