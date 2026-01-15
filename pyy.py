import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("adventures")
window.geometry("900x900")
window.resizable(False, False)

FILe = Image.open("hhh.png")
FILe = FILe.resize(size=[900,900])
FILe = ImageTk.PhotoImage(FILe)

<<<<<<< HEAD
x = StringVar()

=======
>>>>>>> d4d9593c5ffa2d351d8f5f35006222a04f8c3010


picture = Label(master= window, image=FILe)
picture.pack()
label = Label(picture, text="what's your name? type below", font=("Courier", 28), wraplength= 800, bg="forest green", fg="white")
label.place(relx = .17 , rely = .05)
my_response = Entry(picture, width=30, font=("Helvetica", 28))
my_response.place(relx = .16 , rely = .25)
name = my_response
my_button = Button(picture, text="start game?", font=("Courier", 28), fg="white", bg="forest green", relief="ridge")
my_button.place(relx = .35 , rely = .35)
<<<<<<< HEAD

window.wait_variable(x)
my_button.config(command= lambda: my_button.destroy())
my_button.destroy()

FILe = Image.open("hm.png")
FILe = FILe.resize(size=[900,900])
FILe = ImageTk.PhotoImage(FILe)
picture.config(image=FILe)
buttontwo = Button(window, text="moisturize", font=("Courier", 28), fg="white", bg="forest green")
buttontwo.place(relx = .5 , rely = .5)
window.mainloop()
=======
window.mainloop()

>>>>>>> d4d9593c5ffa2d351d8f5f35006222a04f8c3010
