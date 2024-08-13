# bryan block 7/30/2024 1:53 PM
# Prepper manager

import numpy as np
import tkinter as Tk
from tkinter import *
from tkinter import ttk

#global veriables
Difficulty = "easy"

# declares Class Item
class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}({self.weight})"





# Item Class Objects Declrations

# declares the AxeItem from the Item Class
AxeItem = Item("axe" , 7)

SwordItem = Item("Sword", 5)



# declares the checked item varible which is used to check weight
CheckedItem = AxeItem


def StartGame():
    print("game starts")


    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


# checks the weight of objects in the item class
def checkItemweight():
    if CheckedItem.weight > 20:
        print("over weight")
    else:
        print("you aquired " + CheckedItem.name)

# checsk difficulty of the game.
def DifficultyCheck():
    #decalre Difficulty as a Global varible
    global  Difficulty
    Difficulty = input()

    if Difficulty.lower() or Difficulty.upper() == "hard":
        print("are you sure type yes")
        Confirm = input()
        if Confirm.upper() or Confirm.lower() == "yes":
            StartGame()
            return

    if Difficulty.lower() or Difficulty.upper() == "easy":
        print("are you sure type yes")
        Confirm = input()
        if Confirm.upper() or Confirm.lower() == "yes":
            StartGame()
            return


    if Difficulty.lower() or Difficulty.upper() == "normal":
        print("are you sure type yes")
        Confirm = input()
        if Confirm.upper() or Confirm.lower() == "yes":
            StartGame()
            return






# start program

print("welcome to pirate cove")
print("please enter game difficulty, hard ,easy, or normal.")

DifficultyCheck()




