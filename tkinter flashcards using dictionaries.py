#importing everything from the tkinter library
from tkinter import *

import random

#creating a window object
window = Tk()
window.title("Flash Cards - Object Oriented Programming")


flashcard_definitions = {
    "Object-oriented programming": "Designing a program by discovering objects, their properties, and their relationships",
    "Class": "A blueprint or template for an object you want in a program",
    "Attribute": "Characteristics of an object (eg if the object was a human, an attribute could be age)",
    "Object": "Uses attributes and methods from the class so it behaves the same way as other objects derived from the same class",
    "Method": "A function used by the object (eg if the object was a human, a method could be 'walk')",
    "Inheritance": "Making use of a parent class' methods / attributes in a child class",
    "Instantiation": "The creation of an object from a class"}

#text box for displaying the definitions
definition_box = Text(window, width = 20, height = 15, wrap = WORD, bg = "pink")
definition_box.grid(row = 1, rowspan = 7, column = 5, sticky = W)


def display_def(definition):
    definition_box.delete(0.0,END)
    definition_box.insert(END,definition)

def clear():
    definition_box.delete(0.0,END)

def random_def():
    definition_box.delete(0.0,END)
    definition = random.choice((list(flashcard_definitions.items())))
    definition_box.insert(END,definition)
    
Label(window, text = "Pick a term: ").grid(row =  0, column = 1, sticky = W)
Label(window, text = "Definition: ").grid(row = 0, column = 5, sticky = W)

#buttons with terms that have corresponding definitions that can be displayed when clicked
Button(window, text = "Object-oriented programming", command = lambda : display_def(flashcard_definitions["Object-oriented programming"])).grid(row = 1, column = 1, sticky = W)
Button(window, text = "Class", command = lambda: display_def(flashcard_definitions["Class"])).grid(row = 2, column = 1, sticky = W)
Button(window, text = "Attribute", command = lambda: display_def(flashcard_definitions["Attribute"])).grid(row = 3, column = 1, sticky = W)
Button(window, text = "Object", command = lambda: display_def(flashcard_definitions["Object"])).grid(row = 4, column = 1, sticky = W)
Button(window, text = "Method", command = lambda: display_def(flashcard_definitions["Method"])).grid(row = 5, column = 1, sticky = W)
Button(window, text = "Inheritance", command = lambda: display_def(flashcard_definitions["Inheritance"])).grid(row = 6, column = 1, sticky = W)
Button(window, text = "Instantiation", command = lambda: display_def(flashcard_definitions["Instantiation"])).grid(row = 7, column = 1, sticky = W)



#generates a random term and definition from the list
Button(window, text = "Random", command = random_def).grid(row = 7, column = 2, sticky = W)

#button to clear the text box window
Button(window, text = "Clear", command = clear).grid(row = 7, column = 3, sticky = W)


#loop to keep the window on the screen 
window.mainloop()
