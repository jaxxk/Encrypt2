from Tkinter import *

root = Tk()

def printname(event):
    print 'Hello my name is jordode'

button1 = Button(root, text="Print my name")
button1.bind("<Button-1>", printname)
button1.pack()

root.mainloop()