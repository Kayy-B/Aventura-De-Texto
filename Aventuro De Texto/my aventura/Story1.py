from tkinter import *
window=Tk()

text = Text(window, height=37)
text.pack()

text.insert('1.0', 'This is a Text widget demo')


btn=Button(window, text="Left", fg='blue', bg='black', font=("Helvetica", 19))
btn.place(x=230, y=650)
btn1=Button(window, text="Right", fg="blue",bg='pink', font=("Helvetica", 19))
btn1.place(x=780, y = 650)
btn2=Button(window, text="Continue", fg = "blue",bg='red', font=("Helvetica",19))
btn2.place(x = 490, y = 650)



window.title('Hello World')
window.geometry("1100x800")
window.mainloop()