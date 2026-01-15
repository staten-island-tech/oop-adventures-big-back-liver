
import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("Button Example")
window.geometry("900x900")
window.resizable(False, False)
image = Image.open("mukbang.png")
image = image.resize(size=[900,900])
image = ImageTk.PhotoImage(image)

picture = Label(master= window, image=image)
picture.pack()

my_button = Button(window, text="Eat with feet", font=("Arial", 16), bg="aliceblue", fg="black", relief="raised", 
padx=50, pady=15)
my_button.place(relx = .4 , rely = .2)
my_button2 = Button(window, text="stop eating", font=("Arial", 16), bg="lightsalmon", fg="black", relief="raised", 
padx=10, pady=5)
my_button2.place(relx = .4 , rely = .9)



lable = Label(window, text="", wraplength= 800)
lable.pack()
window.mainloop()