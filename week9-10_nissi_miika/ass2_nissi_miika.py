# Small calculator with Python3
#
# Assignment 2, Week 9-10, Miika Nissi

import tkinter
import math

class Calculator:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry()
        root.configure(bg="#2a2a2a")
        self.e = tkinter.Entry(root, bg="#2a2a2a", fg="white", width=25)
        self.e.grid(row=0, column=0, columnspan=4, pady=6)
        self.e.focus_set()

        tkinter.Button(root, text="=", width=3, bg="#CC8400", fg="white", command=lambda:self.equals()).grid(row=5, column=3)
        tkinter.Button(root, text="+", width=3, bg="#CC8400", fg="white", command=lambda:self.action("+")).grid(row=4, column=3)
        tkinter.Button(root, text="-", width=3, bg="#CC8400", fg="white", command=lambda:self.action("-")).grid(row=3, column=3)
        tkinter.Button(root, text="*", width=3, bg="#CC8400", fg="white", command=lambda:self.action("*")).grid(row=2, column=3)
        tkinter.Button(root, text="/", width=3, bg="#CC8400", fg="white", command=lambda:self.action("/")).grid(row=1, column=3)
        tkinter.Button(root, text="C", width=3, bg="#CC8400", fg="white", command=lambda:self.clearAll()).grid(row=1, column=0)
        tkinter.Button(root, text="(", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action("(")).grid(row=1, column=1)
        tkinter.Button(root, text=".", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(".")).grid(row=5, column=2)
        tkinter.Button(root, text=")", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(")")).grid(row=1, column=2)
        
        tkinter.Button(root, text="0", width=10, bg="#2a2a2a", fg="white", command=lambda:self.action(0)).grid(row=5, column=0, columnspan=2)
        tkinter.Button(root, text="1", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(1)).grid(row=4, column=0)
        tkinter.Button(root, text="2", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(2)).grid(row=4, column=1)
        tkinter.Button(root, text="3", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(3)).grid(row=4, column=2)
        tkinter.Button(root, text="4", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(4)).grid(row=3, column=0)
        tkinter.Button(root, text="5", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(5)).grid(row=3, column=1)
        tkinter.Button(root, text="6", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(6)).grid(row=3, column=2)
        tkinter.Button(root, text="7", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(7)).grid(row=2, column=0)
        tkinter.Button(root, text="8", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(8)).grid(row=2, column=1)
        tkinter.Button(root, text="9", width=3, bg="#2a2a2a", fg="white", command=lambda:self.action(9)).grid(row=2, column=2)


    def action(self, arg):
        self.e.insert(tkinter.END, arg)

    def clearAll(self):
        self.e.delete(0, tkinter.END)

    def equals(self):
        try: 
            self.value = eval(self.e.get())
        except:
            self.e.delete(0, tkinter.END)
            self.e.insert(0, "Error!")
        else:
            self.e.delete(0, tkinter.END)
            self.e.insert(0, self.value)

root = tkinter.Tk()
calc = Calculator(root)
root.mainloop()
