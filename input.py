from tkinter import *

# create window
root = Tk()

e = Entry(root, width=50, fg="blue") 
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()