# bryan block 7/30/2024 1:53 PM
# Prepper manager
import os
import tkinter as tk
import os.path as OS
from tkinter import Menu
from tkinter import *
import xml.etree.cElementTree as ET
import ttkbootstrap as ttk
import numpy as np
import json as pym
import yaml as pyaml

ItemIDNum = 0

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

            global ItemIDNum

            ItemInstance = Item

            # if Item des num = amount of entries in file the ++
            ItemDesNum = 4

            # on the function initiilazled gets the inputs from the text boxes in parent function
            ItemTitle = ItemName.get(1.0, "end-1c",)
            ItemWeightInp = ItemWeight.get(1.0, "end-1c")
            ItemQuanityinp = ItemQuanity.get(1.0, "end-1c")

            # Save System for items into items.bpm

            ItemsInfo = {
                "Title": ItemTitle,
                "Weight": ItemWeightInp,
                "Quanity": ItemQuanityinp,
            }

            # integer value that incremnts with ID Number

            # Converts ITemIDNum to string
            IDNum = str(ItemIDNum)

            # Creates a dict
            Itemdata = {
                "ItemID" + " " + IDNum :  [ItemsInfo]
            }

            ItemIDNum + 1

            # if items.bpm exists the prgram will use this line
            if OS.exists("Items.yaml"):

                # appends the document so that previous data will stay



                with (open("Items.yaml", "r") as jsonFile):
                    data = pyaml.safe_load(jsonFile)

                data["location"] = "NewPath"

                with open("Items.yaml", "a") as jsonFile:
                    pyaml.dump(data, jsonFile)


                    # closes the write
                    jsonFile.close()

                    # closes window
                    ItemaddWindowTK.destroy()

            # else used for first time writing to a new project
            else:
                with open("Items.yaml", "w") as saveitems:

                    # creates the info that will be saved in ItemsData
                                 
                    # Dumps the array
                    pyaml.safe_dump(Itemdata, saveitems)


                    # erase later
                    # converts array to string


                    # writes araray
                    # saveitems.write(ItemJsonSave)
                    
                    


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

        # declares ItemInfoFrame
        ItemInfoFrame = ttk.Frame(root, height=400, width=400, bootstyle="info" )

        ItemInfoScrollBar = tk.Scrollbar(ItemInfoFrame, width=100, orient="horizontal")
        ItemInfoScrollBar.place(x=170, y=0)

        # creates Item Buttons
        def ItemButtonCreation():
            if OS.exists("Items.yaml"):
                # Opening JSON file
                with open('Items.yaml', "r") as f:
                    prime_service = pyaml.safe_load(f)





                # returns JSON object as
                # a dictionary

                    # Iterating through the json
                    # list


                    # the array that is incremented
                    ArrayVar = 0

                    IDNumConvert = str(ArrayVar)

                    # converts from json to python and tells the stirng the "Title"






                    def buttoonCreation():
                        # creates the Buttons
                        Itembutton = tk.Button(ItemInfoFrame, text=newdata, width=20)


                        Itembutton.pack()
                        print(f)

                        # Closing file



                # sets the number of buttons depending on objects in the jason file
                    for Itembutton in range(NumButtonLinesB):

                        print(prime_service)
                        # creates the button and gets the index
                        newdata = prime_service["ItemID" + IDNumConvert]["Title"]
                        # for i in datanew['']:
                        print(newdata)

                        # and name then based of of Item Title
                        buttoonCreation()

                        # ARRAY IS INCREMENTED right here
                        ArrayVar = ArrayVar + 1

                        # Closing file
                        f.close()


        # decalres add item button
        AddItemButton = Button(CanvasFrame, text="Add Item", command=ItemAddWindow)

        # creates the add item button
        AddItemButton.pack(side=LEFT,)
        AddItemButton.propagate(0)

        label = Label(BackGroundCanvas)
        label.pack()


        ttk.Button(CanvasFrame, bootstyle="warning")


        dnd = DragManager()

        # add dragable items in this lines
        dnd.add_draggable(label)
        dnd.add_draggable(CanvasFrame)
        dnd.add_draggable(ItemInfoFrame)

        ItemInfoFrame.pack(side=RIGHT)

        BackGroundCanvas.pack(side=LEFT)
        CanvasFrame.pack()

        ItemButtonCreation()

        # starts the tkinter main loop for rendering.
        root.mainloop()

    # checsk to see if Item.bpm file exists.
    if OS.exists("Items.yaml"):
        # opens the Items.BPM file for reading
        with open('Items.yaml', "r") as ItemDataRead:

            # reads the lines of Items.BPM via the varibale ItemDataRead
            Lines = pyaml.safe_load(ItemDataRead)

            #Gets the lentgh of the items and puts them into the number of lines varaible
            NumButtonLinesB = len(Lines)
            print(NumButtonLinesB)

            # prints the values of ItemDataRead via Lines vraible
            print(Lines)

        #calls the create main UI Function
        createMainUI()

        ItemDataRead.close()

    else:
        createMainUI()

#the program runs this function on the start of the program


def FirstStart():



    if OS.exists("Registration.xml"):
        print("file exists")
        StartPerpperBackpackerMananger()




    else:
        #def regwindowcreate():
            # starts the tkinter window
        RegFrame = tk.Tk()
        RegFrame.title("first start")
        RegFrame.geometry("400x400")

            # gets the input of the owner

            # TextBox Creation

        inputnametxt = tk.Text(RegFrame, height=2, width=20, )

        inputnametxt.insert("insert", "your name")

        inputnametxt.place(x=10, y=0)





        def getOwnerInput():
            # declares inp to to get whatever is in the textbox  inputnametext
            inp = inputnametxt.get(1.0, "end-1c")

            # opens owner info.xml
            Ownerinfo = open("Registration.xml", "w")

            # gets the owner input and saves to file.
            Ownerinfo.write(str(inp))
            Ownerinfo.close()

            # destroys the frame
            RegFrame.destroy()
            # calls first start function agin with registartion already save in previous function
            FirstStart()

        #regwindowcreate()
        # creates the get owner info button
        getOwnerInfoButton = tk.Button(RegFrame, text="confirm", command=getOwnerInput)
        getOwnerInfoButton.place(x=300, y=350)

        RegFrame.mainloop()







FirstStart()