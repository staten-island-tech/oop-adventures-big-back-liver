
import tkinter
from tkinter import *
window = Tk()
window.title("Button Example")
my_button = Button(window, text="What would you like to eat?", font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=10, pady=5)
my_button.pack()

resposnes = Entry(window, width= 30)
resposnes.pack()

lable = Label(window, text="", wraplength= 800)
lable.pack()
window.mainloop()