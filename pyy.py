import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("oop adventures")
window.geometry("1500x900")
window.resizable(False, False)

FILe = Image.open("name.jpg")
FILe = FILe.resize(size=[1500,900])
picture = Label(master= window, image="")
label = Label(window, text="what's your name? type below", font=("Helvetica", 28), wraplength= 800)
label.pack(pady=10)
my_response = Entry(window, width=30, font=("Helvetica", 28))
my_response.pack(pady=10)
name = my_response
my_button = Button(window, text="start game?", font=("Courier", 28), fg="white", bg="midnight blue", relief="ridge")
my_button.pack(pady=10)
window.mainloop()

