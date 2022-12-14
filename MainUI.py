from tkinter import *
from tkinter import Widget, ttk

class LaunchMainUi(Widget):

    def __init__(self):
        Widget.__init__(self, None, None)

        self.attributes('-geometry', '250x300')
        
        self.label = ttk.Label(text='Main')
        self.button = ttk.Button(text='Click!', command=self.setLabelText)

        self.label.pack()
        self.button.pack()
    
    def setLabelText(self):
        self.label["text"] = "Hello"
    

