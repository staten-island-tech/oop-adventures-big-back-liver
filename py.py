
import tkinter
from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title("Button Example")
window.geometry("900x900")
window.resizable(False, False)

my_button = Button(window, text="Eat with feet", font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=100, pady=50)
my_button.pack()
my_button2 = Button(window, text="stop eating", font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=10, pady=5)
my_button2.pack()

image = Image.open("mukbang.png")
image = image.resize(size=[900,900])
image = ImageTk.PhotoImage(image)

picture = Label(master= window, image=image)
picture.pack()

lable = Label(window, text="", wraplength= 800)
lable.pack()
window.mainloop()