import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("oop adventures")
window.geometry("900x900")
window.resizable(False, False)

FILe = Image.open("hhh.png")
FILe = FILe.resize(size=[900,900])
FILe = ImageTk.PhotoImage(FILe)

x = StringVar()
 


picture = Label(master= window, image=FILe)
picture.pack()
label = Label(picture, text="what's your name? type below", font=("Courier", 28), wraplength= 800, bg="forest green", fg="white")
label.place(relx = .17 , rely = .05)
my_response = Entry(picture, width=30, font=("Helvetica", 28))
my_response.place(relx = .16 , rely = .25)
name = my_response
my_button = Button(picture, text="start game?", font=("Courier", 28), fg="white", bg="forest green", relief="ridge", command= lambda: x.set('werwrewrrw'))
my_button.place(relx = .35 , rely = .35)

window.wait_variable(x)
FILe = Image.open("hm.png")
FILe = FILe.resize(size=[900,900])
FILe = ImageTk.PhotoImage(FILe)
picture.config(image=FILe)
window.mainloop()
""" 
from app import base
class backgroundgame(Frame):
    def __init__(self, masterx = base, imagex = "hm.png"):
        super().__init__(master = masterx ,image = imagex)
        self.picter = Image.open(imagex)
        self.picter = self.picter.resize(size="900x900")
        self.config(imagex = self.picter)
 """
