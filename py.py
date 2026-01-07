import tkinter as tk
window = tk.Tk()
window.title("eat")
window.geometry("200x200") 
window.resizable(False, False)
my_button = tk.Button(window, text = "", font=("Courier", 24), bg = "white", fg="black", relief = "raised", padx=10, pady = 5)
window.mainloop()