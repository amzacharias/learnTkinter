#!/usr/bin/python3
"""
Title: Intro to using tkinter to make a GUI; making a window
Author: Amanda Zacharias
Date Created: 08/13/2023
Date Modified: 08/13/2023
Version: python 3.11.4
Note: 
Following this tutorial: https://youtu.be/ibf5cx221hk
"""

# Dependencies
import tkinter as tk

# Instantiate window
root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

# Basics with packing
label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10, pady=10)

myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

button = tk.Button(root, text="Click Me!", font=("Arial", 16))
button.pack(padx=10, pady=10)

# Button grid
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill=tk.X)

# Place
anotherBtn = tk.Button(root, text="TEST")
anotherBtn.place(x=200, y = 350, height = 100, width = 100)


root.mainloop()

