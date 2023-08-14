#!/usr/bin/python3
"""
Title: Intro to using tkinter to make a GUI; adding functionality
Author: Amanda Zacharias
Date Created: 08/13/2023
Date Modified: 08/13/2023
Version: python 3.11.4
Note: 
Following this tutorial: https://youtu.be/ibf5cx221hk
"""

# Dependencies
import tkinter as tk
from tkinter import messagebox

# Class
class MyGUI: 

    def __init__(self):

            self.root = tk.Tk()
            
            # Menu
            self.menubar = tk.Menu(self.root)

            self.filemenu = tk.Menu(self.menubar, tearoff=0) # tearoff=0 means no dashed line at top
            self.filemenu.add_command(label="Close", command=self.onClosing)
            self.filemenu.add_separator()
            self.filemenu.add_command(label="Close without question", command=exit)

            self.actionmenu = tk.Menu(self.menubar, tearoff=0)
            self.actionmenu.add_command(label="Show Message", command=self.showMessage)

            self.menubar.add_cascade(menu=self.filemenu, label="File")
            self.menubar.add_cascade(menu=self.actionmenu, label="Action")
            
            self.root.config(menu=self.menubar)

            # Main app
            self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
            self.label.pack(padx=10, pady=10)

            self.textbox = tk.Text(self.root, font=("Arial", 16))
            self.textbox.bind("<KeyPress>", self.shortcut)
            self.textbox.pack(padx=10, pady=10)

            self.checkState = tk.IntVar()

            self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 16), variable=self.checkState)
            self.check.pack(padx=10, pady=10)

            self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.showMessage)
            self.button.pack(padx=10, pady=10)

            self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 18), command=self.clear)
            self.clearbtn.pack(padx=10, pady=10)

            self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

            self.root.mainloop()


    def showMessage(self): 
        if (self.checkState.get() == 0): 
             print(self.textbox.get("1.0", tk.END)) # (1.0, tk.END) are indexes for text to show, start to end
        else: 
             messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))


    def shortcut(self, event): 
         # left meta + return as shortcut to showing the message
         if event.state == 8 and event.keysym == "Return": 
              self.showMessage()


    def onClosing(self): 
         if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"): 
              self.root.destroy()


    def clear(self): 
        self.textbox.delete('1.0', tk.END)


MyGUI()





