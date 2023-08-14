
#!/usr/bin/python3
"""
Title: Make a response data entry gui
Author: Amanda Zacharias
Date Created: 08/14/2023
Date Modified: 08/14/2023
Version: python 3.11.4
Note: 
Following this tutorial: https://www.youtube.com/watch?v=vusUfPBsggw
"""

# Dependencies
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Functions
def enterData(): 
    accepted = acceptVar.get()
    if accepted == "Accepted": # If user accepted the terms & conditions
        # User info
        firstName = firstNameEntry.get()
        lastName = lastNameEntry.get()

        if firstName and lastName: # If firstName and lastName are not empty
            title = titleComboBox.get()
            age = ageSpinBox.get()
            nationality = nationalityComboBox.get()
            print(firstName, lastName, title, age, nationality)

            # Course info
            registrationStatus = regStatusVar.get()
            numCourses = numCoursesSpinBox.get()
            numSemesters = numSemestersSpinBox.get()
            print(registrationStatus, numCourses, numSemesters)
        else: 
            tk.messagebox.showwarning(title="Error", message="First and last names are required.")
    else: 
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

# Root Window
root = tk.Tk()
root.title("Date Entry Form")

frame = tk.Frame(root)
frame.pack()

# User information
userInfoFrame = tk.LabelFrame(frame, text="User Information")
userInfoFrame.grid(row=0, column=0, padx=20, pady=10)

firstNameLabel = tk.Label(userInfoFrame, text="First name")
firstNameLabel.grid(row=0, column=0)
lastNameLabel = tk.Label(userInfoFrame, text= "Last name")
lastNameLabel.grid(row=0, column=1)

firstNameEntry = tk.Entry(userInfoFrame)
firstNameEntry.grid(row=1, column=0)
lastNameEntry = tk.Entry(userInfoFrame)
lastNameEntry.grid(row=1, column=1)

titleLabel= tk.Label(userInfoFrame, text="Title")
titleComboBox = ttk.Combobox(userInfoFrame, values=["", "Dr.", "Mrs.", "Ms.", "Mr."])
titleLabel.grid(row=0, column=2)
titleComboBox.grid(row=1, column=2)

ageLabel = tk.Label(userInfoFrame, text="Age")
ageSpinBox = tk.Spinbox(userInfoFrame, from_=0, to=120)
ageLabel.grid(row=2, column=0)
ageSpinBox.grid(row=3, column=0)

nationalityLabel = tk.Label(userInfoFrame, text="Nationality")
nationalityComboBox = ttk.Combobox(userInfoFrame, values=["Africa", "Antartica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationalityLabel.grid(row=2, column=1)
nationalityComboBox.grid(row=3, column=1)

for widget in userInfoFrame.winfo_children(): 
    widget.grid_configure(padx=10, pady=5)

# Course registration
coursesFrame = tk.LabelFrame(frame, text = "Course Information")
coursesFrame.grid(row=1, column=0, sticky = "news", padx=20, pady=10)

registeredLabel = tk.Label(coursesFrame, text="Registration status")
regStatusVar = tk.StringVar(value="Not Registered")
registeredCheck = tk.Checkbutton(coursesFrame, text="Currently Registered", 
                                 variable=regStatusVar, onvalue="Registered", offvalue="Not Registered")
registeredLabel.grid(row=0, column=0)
registeredCheck.grid(row=1, column=0)

numCoursesLabel = tk.Label(coursesFrame, text="# Completed Courses")
numCoursesSpinBox = tk.Spinbox(coursesFrame, from_=0, to="infinity")
numCoursesLabel.grid(row=0, column=1)
numCoursesSpinBox.grid(row=1, column=1)

numSemestersLabel = tk.Label(coursesFrame, text="# Completed Semesters")
numSemestersSpinBox = tk.Spinbox(coursesFrame, from_=0, to="infinity")
numSemestersLabel.grid(row=0, column=2)
numSemestersSpinBox.grid(row=1, column=2)

for widget in coursesFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
termsFrame = tk.LabelFrame(frame, text="Terms & Conditions")
termsFrame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

acceptVar = tk.StringVar(value="Not Accepted")
termsCheck = tk.Checkbutton(termsFrame, text="I accept the terms and conditions", 
                            variable=acceptVar, onvalue="Accepted", offvalue="Not Accepted")
termsCheck.grid(row=0, column=0)

# Button
button = tk.Button(frame, text="Enter data", command = enterData)
button.grid(row=3, column=0, sticky = "news", padx=20, pady=10)

root.mainloop()
