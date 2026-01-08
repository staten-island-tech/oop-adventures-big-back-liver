import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("oop adventures")
window.geometry("1500x900")
window.resizable(False, False)

FILe = Image.open("openingscreen.jpg")
FILe = FILe.resize(size=[1500,900])
FILe = ImageTk.PhotoImage(FILe)

picture = Label(master= window, image=FILe)
picture.pack()
label = Label(picture, text="what's your name? type below", font=("Helvetica", 28), wraplength= 800)
label.place(relx = .35 , rely = .1)
my_response = Entry(picture, width=30, font=("Helvetica", 28))
my_response.place(relx = .3 , rely = .2)
name = my_response
my_button = Button(picture, text="start game?", font=("Courier", 28), fg="white", bg="midnight blue", relief="ridge")
my_button.place()
window.mainloop()

