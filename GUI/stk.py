# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:56:22 2019

@author: Administrator
"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.edit = tk.Entry(self)
        self.edit['text'] = 'input something'
        self.edit.pack(side='top')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        print(self.edit.get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()