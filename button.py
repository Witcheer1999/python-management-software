from tkinter import *

# create window
root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click me", command=myClick)
myButton.pack()

root.mainloop()