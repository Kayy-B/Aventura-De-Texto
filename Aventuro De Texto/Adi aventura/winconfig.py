from tkinter import *
class mainWindow():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1280x720")
      self.win.configure(bg='')
      self.win.title("Story")
      self.win["background"]="#35382F"
class secondWindow():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1280x720")
      self.win.title("Story")
      self.win["background"]="#30D5C8"

class story1Window():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1280x720")
      self.win.title("Story")
      self.win["background"]="#ffffff"

class Mbar():
   def __init__(self, win):
      self.win = win
   def popup(self):
      pass
   def nav(self):
      menubar = Menu(self.win)
      abmenu = Menu(menubar)
      abmenu.add_command(label="About Game", command= self.popup())
      abmenu.add_separator()
      abmenu.add_command(label="Our Team", command= self.popup())
      menubar.add_cascade(label="About Us", menu=abmenu)
      self.win.config(menu=menubar)