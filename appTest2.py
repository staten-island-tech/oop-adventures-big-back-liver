import tkinter
from tkinter import *
from PIL import Image, ImageTk
base = Tk()
base.geometry("900x900")
base.resizable(False, True)
specialsring = StringVar()
class backgound(Frame):
    
    def __init__(self, masterx = base, imagex = "backgroundbedroom.jpg" ):
        super().__init__(master= masterx)
        self.pack()
        

        self.picter = Image.open( "background/" + imagex)
        self.picter = self.picter.resize([900,900])
        tkinterconver = ImageTk.PhotoImage(self.picter)

        self.label = Label(master = self, image= tkinterconver)
        self.label.storage = tkinterconver
        
        self.label.pack(expand= True, fill= "both")
        masterx.update()

    def kys(self):
        self.destroy()


def anim( name, Ftype, frams):
    
    for i in range(0, frams+1):
        
        base.update()
        bith = str(i)
        blud = name + bith + Ftype
        print(blud)
        TheBackground = backgound(masterx = base, imagex= blud)
        base.update()
        base.after(500)
        base.update()
        TheBackground.kys()
        
        

anim(name="notification1/backgroundlaptopScreenN", Ftype= ".png", frams= 5)
TheBackground = backgound(masterx = base, imagex= "notification1/backgroundlaptopScreenN5.png")
base.mainloop()

