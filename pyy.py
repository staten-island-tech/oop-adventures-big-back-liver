import tkinter
from tkinter import *
window = Tk()
window.title("oop adventures")
window.geometry("1500x900")
window.resizable(False, False)
my_button = Button(window, text="start game?")
my_button.pack()
if my_button == True:
    my_response = Entry(window, width=30)
    my_response.pack()
    name = my_response
