from tkinter import *
import sys
sys.path.insert(0, './Pages')
class mainWindow():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1920x1080")
      self.win.configure(bg='')
      self.win.title("Home")
      self.win["background"]="#35382F"
class secondWindow():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1920x1080")
      self.win.title("Index")
      self.win["background"]="#30D5C8"

class story1Window():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1920x1080")
      self.win.title("Story1")
      self.win["background"]="#ffffff"

class story2Window():
   def __init__(self, win):
      self.win = win
   def set(self):
      self.win.geometry("1920x1080")
      self.win.title("Story2")
      self.win["background"]="#ffffff"

class Mbar():
   def __init__(self, win):
      self.win = win
   def popup(self):
         self.win.destroy()
         self.sys.path.insert(0, './Pages')
         import about_game
   def tea(self):
         self.win.destroy()
         self.sys.path.insert(0, './Pages')
         import about_team
   def nav(self):
      menubar = Menu(self.win)
      abmenu = Menu(menubar)
      abmenu.add_command(label="About Game", command= self.popup)
      abmenu.add_command(label="Our Team", command= self.tea)
      menubar.add_cascade(label="About Us", menu=abmenu)
      self.win.config(menu=menubar)