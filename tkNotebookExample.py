#!usr/bin/env python
#tkNotebook
#Created By: Patrick T. Cossette <cold_soul79078@yahoo.com>

#tkNotebook allows users to make notebook widgets in Tk

#This software may be modified and redistributed, as long as any and all changes made
#From here on are stated, and ("Created By: Patrick T. Cossette <cold_soul79078@yahoo.com>") still remains somewhere
#In the code.

#This software is opensource, and free in hopes that it may be useful, and comes AS IS
#With no warrenty.

"""
    Defines a Notebook class to be used with Tkinter. A Notebook instance
    has the attributes change_tab, add_tab, destroy_tab, and focus_on.

    change_tab:  Internal Function, I don't suggest you call this directly.
    add_tab:     Creates a tab
    destroy_tab: destroys the given tab
    focus_on:    Focuses on the given tab

    The __init__ function creates three frames. One to hold the tabs together,
    one to create the base to parent each tab's children, and one to hold the
    base frame and the tab frame together.

    Each tab is a Label with a default relief of "GROOVE". Each label uses
    event bindings so that change_tab is called with the tab's ID Number as
    an argument. Each tab relief, when selected is set by default to "RAISED"
    
    For an exampe, view the source code, and run the module.

    Created By: Patrick T. Cossette <cold_soul79078@yahoo.com>    

"""

from Tkinter import *
from tkNotebook import Notebook

def demo():
    def adjustCanvas(someVariable = None):
        fontLabel["font"] = ("arial", var.get())
    
    root = Tk()
    root.title("tkNotebook Example")
    note = Notebook(root, width= 400, height =400, activefg = 'red', inactivefg = 'blue')  #Create a Note book Instance
    note.grid()
    tab1 = note.add_tab(text = "Tab One")                                                  #Create a tab with the text "Tab One"
    tab2 = note.add_tab(text = "Tab Two")                                                  #Create a tab with the text "Tab Two"
    tab3 = note.add_tab(text = "Tab Three")                                                #Create a tab with the text "Tab Three"
    tab4 = note.add_tab(text = "Tab Four")                                                 #Create a tab with the text "Tab Four"
    tab5 = note.add_tab(text = "Tab Five")                                                 #Create a tab with the text "Tab Five"
    Label(tab1, text = 'Tab one').grid(row = 0, column = 0)                                #Use each created tab as a parent, etc etc...
    Label(tab1, text = "When something is changed on a tab,\ngoing to a different tab and back\nwill not reset, or effect it in any way.", font = ("Comic Sans MS", 12, "italic")).grid()
    var = IntVar()
    var.set(10)
    scale = Scale(tab1, font = ("arial", 10), orient = 'horizontal', command = adjustCanvas, variable =var).grid()
    fontLabel = Label(tab1, text = "TEXT", font = ("Arial", 10))
    fontLabel.grid()
    Label(tab2, text = 'Tab Two\n\n(Has focus first by using the focus_on attribute)\n\nThe tabs are colored red and blue via\nthe Notebook options. The default\nvalues are black on black :P', font = ("Comic Sans MS", 12, "italic")).grid()
    Button(tab3, text = 'Destroy Tab Four!', command = lambda:note.destroy_tab(tab4)).grid()
    Label(tab3, text = "Destroying a tab will remove it,\nand competely destoy all child widgets.\nOnce you destroy a tab, you have to recreate it\ncompletely in order to get it back.", font = ("Comic Sans MS", 12, "italic")).grid()
    Label(tab4, text = 'Tab 4').grid()
    Button(tab5, text = 'Tab One', command = lambda:note.focus_on(tab1)).grid(pady = 3)
    Button(tab5, text = 'EXIT', width = 23, command = root.destroy).grid()
    note.focus_on(tab2)
    root.mainloop()

if __name__ == "__main__":
    demo()
