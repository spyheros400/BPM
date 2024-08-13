# bryan block 7/30/2024 1:53 PM
# Prepper manager

import tkinter as tk
import os.path as OS
from tkinter import Menu
from tkinter import *
from RoundedTk import *
import ttkbootstrap as ttk

# global veriables
Name = "NONAME"

# declares Class Item1
class Item:
    def __init__(self, name, weight, quanity):
        self.name = name
        self.weight = weight
        self.quanity = quanity

    def __str__(self):
        return f"{self.name}({self.weight})"

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

    print("starting Program")
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
    CanvasFrame = Frame(root, height=800, width=100, bg="#787676")
    # mounts to the left of the screen
    CanvasFrame.pack(side=LEFT)

    # declares backpackinfoframe
    BackPackInfoFrame = Frame(root, height=200, width=200,bg="#787676")



    # decalres add item button
    AddItemButton = Button(CanvasFrame, text="Add Item",)

    # creates the add item button
    AddItemButton.pack(side=RIGHT,)
    AddItemButton.place(x=5, y=5)

    label = Label(BackGroundCanvas)
    label.pack()

    BackPackInfoFrame.pack(side=RIGHT)
    ttk.Button(BackPackInfoFrame,)


    dnd = DragManager()

    # add dragable items in this lines
    dnd.add_draggable(label)
    dnd.add_draggable(CanvasFrame)
    dnd.add_draggable(BackPackInfoFrame)

    BackGroundCanvas.pack(side=LEFT)
    CanvasFrame.pack()

    # starts the tkinter main loop for rendering.
    root.mainloop()

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