# Small math game with Python3
#
# Assignment 1, Week 9-10, Miika Nissi

import tkinter
import random

class Game(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        
        self.welcome_text = tkinter.Label(self, text="Fun Math Game!")
        self.welcome_text.grid(row=0, sticky="nsew", padx=10, pady=10, columnspan = 6)
        self.instruction_text = tkinter.Label(self, text="Answer correctly to earn points.")
        self.instruction_text.grid(row=2, sticky="nsew", padx=20, pady=10, columnspan = 6)
        
        self.points_label = tkinter.Label(self, text="Points:", fg="green")
        self.point_var = tkinter.IntVar()
        self.point_label = tkinter.Label(self, textvariable=self.point_var, fg="green")

        self.a_var = tkinter.IntVar()
        self.b_var = tkinter.IntVar()
        self.c_var = tkinter.IntVar()
        self.a_label=tkinter.Label(self, textvariable=self.a_var)
        self.b_label=tkinter.Label(self, textvariable=self.b_var)
        
        self.sign = tkinter.Label(self, text="+")
        self.elc = tkinter.Label(self, text="Answer:")
        self.ec = tkinter.Entry(self)
        
        self.getEquation()

        self.result_label = tkinter.Label(self, text="")
        
        self.button = tkinter.Button(self, 
                text="Result", 
                command=self.checkEquation)


        self.points_label.grid(row=1, column=2)
        self.point_label.grid(row=1, column=3)
        self.a_label.grid(row=3, column=2)
        self.sign.grid(row=3, column=3)
        self.b_label.grid(row=3, column=4)

        self.elc.grid(row=4, column=0, columnspan=2, pady=6, padx=6)
        self.ec.grid(row=4, column=2, columnspan=2, pady=6, padx=6)
        self.button.grid(row=4, column=4, columnspan=2, pady=6, padx=6)

        self.result_label.grid(row=5, column=0, columnspan=6, pady=6, padx=6)

    def getEquation(self):
        self.a_var.set(random.randint(1,50))
        self.b_var.set(random.randint(1,50))
        self.c_var.set(self.a_var.get() + self.b_var.get())

    def checkEquation(self):
        x = str(self.ec.get())
        y = str(self.c_var.get())
        a = str(self.a_var.get())
        b = str(self.b_var.get())
        # comparing x == y does not work for some reason, comparing str() works
        if (x == y):
            self.result_label.config(text="Correct Answer! " + a + " + " + b + " = " + y, fg="green")
            self.point_var.set(self.point_var.get() + 1)
        else:
            self.result_label.config(text="Wrong Answer! " + a + " + " + b + " = " + y, fg="red")
        self.getEquation()

        

root = tkinter.Tk()
root.title("Math Game")
root.resizable()
game = Game(root)
game.grid()
root.mainloop()
