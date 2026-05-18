from tkinter import *
from datetime import date

def age():
    y = date.today().year - int(year.get())
    result.config(text="Age: " + str(y))

root = Tk()

Label(root, text="Birth Year").pack()
year = Entry(root)
year.pack()

Button(root, text="Calculate", command=age).pack()

result = Label(root, text="")
result.pack()

root.mainloop()