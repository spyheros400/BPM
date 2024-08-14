# bryan block 7/30/2024 1:53 PM
# Prepper manager

import tkinter as tk
import os.path as OS
from tkinter import Menu
from tkinter import *
from RoundedTk import *
import xml.etree.cElementTree as ET
import ttkbootstrap as ttk
import numpy as np
import json as pym


# global veriables
Name = "NONAME"

# function that starts the program.
def StartPerpperBackpackerMananger():

    # draggable funrctions for canvvas

    class DragManager():
        def add_draggable(self, widget):
            widget.bind("<ButtonPress-1>", self.on_start)
            widget.bind("<B1-Motion>", self.on_drag)
            widget.bind("<ButtonRelease-1>", self.on_drop)
            widget.configure(cursor="hand1")

        def on_start(self, event):
            widget = event.widget
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y

        def on_drag(self, event):
            widget = event.widget
            x = widget.winfo_x() - widget._drag_start_x + event.x
            y = widget.winfo_y() - widget._drag_start_y + event.y
            widget.place(x=x, y=y)

        def on_drop(self, event):
            # Find the widget under the cursor and perform necessary actions
            x, y = event.widget.winfo_pointerxy()
            target = event.widget.winfo_containing(x, y)
            try:
                target.configure(image=event.widget.cget("image"))
            except:
                pass


    # declares Class Item (class unused erase later)
    class Item:



        # task count and current is used to generate indentifiers
        task_count = 0
        CurrentCount = 0

        def __init__(self, name, weight, quanity):
            self.name = name
            self.weight = weight
            self.quanity = quanity




        def __str__(self):
            return f"{self.name}{self.weight}{self.quanity}"



    # declares item add window
    def ItemAddWindow():



        def getinput():

            ItemInstance = Item

            # if Item des num = amount of entries in file the ++
            ItemDesNum = 4

            # on the function initiilazled gets the inputs from the text boxes in parent function
            ItemTitle = ItemName.get(1.0, "end-1c",)
            ItemWeightInp = ItemWeight.get(1.0, "end-1c")
            ItemQuanityinp = ItemQuanity.get(1.0, "end-1c")

            # Save System for items into items.bpm

            # if items.bpm exists the prgram will use this line
            if OS.exists("Items.bpm"):

                # appends the document so that previous data will stay
                with open("Items.bpm", "a") as saveitems:

                    # writes a space
                    saveitems.write("\n")

                    # puts items into an array
                    Itemdata = np.array([ItemTitle, ItemWeightInp, ItemQuanityinp])

                    # converts array to string
                    convertTostring = str(Itemdata)

                    # writes araray
                    saveitems.write(convertTostring)

                    # closes the write
                    saveitems.close()

                    # closes window
                    ItemaddWindowTK.destroy()

            # else used for first time writing to a new project
            else:
                with open("Items.bpm", "w") as saveitems:

                    # puts items into an array
                    Itemdata = np.array([ItemTitle, ItemWeightInp, ItemQuanityinp])

                    # converts array to string
                    convertTostring = str(Itemdata)

                    # writes araray
                    saveitems.write(convertTostring)

                    # closes the write
                    saveitems.close()

                    #closes window
                    ItemaddWindowTK.destroy()


        ItemaddWindowTK = tk.Tk()
        ItemaddWindowTK.title("Add Item")
        ItemaddWindowTK.geometry("600x600")

        # creates Item name text
        ItemName = ttk.Text(ItemaddWindowTK, height=1, width=10)
        ItemName.insert("insert", "Item Name", )
        ItemName.place(x=0, y=0)

        # cretes the item weight entry textbox
        ItemWeight = ttk.Text(ItemaddWindowTK, height=1, width=10)
        ItemWeight.insert("insert", "Item Weight")
        ItemWeight.place(x=0, y=40)

        # creates the qunity textbox input
        ItemQuanity = ttk.Text(ItemaddWindowTK, height=1, width=10)
        ItemQuanity.insert("insert", "Quanity")
        ItemQuanity.place(x=90, y=40)

        # declares the Confirm item name button
        ConfirmNameBTn = ttk.Button(ItemaddWindowTK, text="Confirm Item", command=getinput)
        ConfirmNameBTn.place(x=450, y=500)






    print("starting Program")

    def createMainUI():
        #  creates the program window
        root = tk.Tk()
        root.title("Prepper Backpack Manager")
        root.geometry("800x650")

        # declares the top menu bar
        topmenubar = Menu(root)
        root.config(menu = topmenubar)

        # creates the menu bar at the top
        filemenu = Menu(root)

        # prevnts the user fro, dragging the top bar away
        filemenu = Menu(topmenubar, tearoff=False)

         # adds the menu to the bar
        filemenu.add_command(
            label='Exit',
            command=root.destroy
        )



        # add the File menu to the menubar and make it visble
        topmenubar.add_cascade(
            label="File",
            menu=filemenu

        )

        # creates the canvas that will have dragable compaonants.
        BackGroundCanvas = tk.Canvas(root, width=800, height=650, bg="#575555")
        # declares the toolbar
        CanvasFrame = ttk.Frame(root, height=800, width=100, bootstyle="info")
        # mounts to the left of the screen
        CanvasFrame.pack(side=LEFT)
        CanvasFrame.propagate(0)

        # declares the top bar for the CanvasFrame
        CanvasFrameTopBar = ttk.Label(CanvasFrame, text="Toolbar", width=20)
        CanvasFrameTopBar.pack(side=TOP)

        # declares backpackinfoframe
        BackPackInfoFrame = ttk.Frame(root, height=200, width=200, bootstyle="info" )



        # decalres add item button
        AddItemButton = Button(CanvasFrame, text="Add Item", command=ItemAddWindow)

        # creates the add item button
        AddItemButton.pack(side=LEFT,)
        AddItemButton.propagate(0)

        label = Label(BackGroundCanvas)
        label.pack()

        BackPackInfoFrame.pack(side=RIGHT)
        ttk.Button(CanvasFrame, bootstyle="warning")


        dnd = DragManager()

        # add dragable items in this lines
        dnd.add_draggable(label)
        dnd.add_draggable(CanvasFrame)
        dnd.add_draggable(BackPackInfoFrame)


        BackGroundCanvas.pack(side=LEFT)
        CanvasFrame.pack()

        # starts the tkinter main loop for rendering.
        root.mainloop()

    # checsk to see if Item.bpm file exists.
    if OS.exists("Items.bpm"):

        # opens the Items.BPM file for reading
        ItemDataRead = open('Items.bpm', 'r')

        # reads the lines of Items.BPM via the varibale ItemDataRead
        Lines = ItemDataRead.readlines()

        # prints the values of ItemDataRead via Lines vraible
        print(Lines)

        #calls the create main UI Function
        createMainUI()
#the program runs this function on the start of the program
def FirstStart():

    if OS.exists("Registration.xml"):
        print("file exists")
        StartPerpperBackpackerMananger()




    else:

        def getOwnerInput():
            # declares inp to to get whatever is in the textbox  inputnametext
            inp = inputnametxt.get(1.0, "end-1c")

            # opens owner info.xml
            Ownerinfo = open("Registration.xml", "w")

            # gets the owner input and saves to file.
            Ownerinfo.write(str(inp))
            Ownerinfo.close()

            # destroys the frame
            frame.destroy()
            # calls first start function agin with registartion already save in previous function
            FirstStart()



        # starts the tkinter window
        frame = tk.Tk()
        frame.title ("first start")
        frame.geometry("400x400")

        # gets the input of the owner


    # TextBox Creation

    inputnametxt = tk.Text(frame,
                    height=2,
                    width=20,)

    inputnametxt.insert("insert", "your name")

    inputnametxt.place(x=10, y=0)


        # creates the get owner info button
    getOwnerInfoButton = tk.Button(frame, text="confirm", command=getOwnerInput)
    getOwnerInfoButton.place(x= 300, y=350)

    frame.mainloop()

FirstStart()