
import tkinter
from tkinter import *
window = Tk()
window.title("Button Example")
my_button = Button(window, text="Eat with feet", font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=100, pady=50)
my_button2 = Button(window, text="Eat with hands", font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=10, pady=5)
my_button.pack()

lable = Label(window, text="", wraplength= 800)
lable.pack()
window.mainloop()