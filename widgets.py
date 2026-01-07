import tkinter
from tkinter import *
from PIL import Image, ImageTk

from app import base

class backgound(Frame):
    
    def __init__(self, masterx = base, imagex = "backgroundspookyforest.jpg" ):
        super().__init__(master = masterx ,image = imagex)
        self.picter = Image.open(imagex)
        self.picter = self.picter.resize(size="1500x900")
        self.config(imagex = self.picter)

    def kys(self):
        self.destroy()





class scenebutton(Button):

    def __init__(self, masterx = base, textx = "Continue", color = "Grey", ifPressed = None):
        super().__init__(master= masterx, text = textx, fg= color, command = lambda: self.switchscreen(ifPressed))
        self.masterx = masterx
        self.textx = textx
        self.color = color
        self.ifPressed = ifPressed
        #if pressed is supposed to be an image path to the next scene
    
    def switchscreen(self):
        self.ifPressed

        global TheBackground 
        TheBackground = backgound(masterx = base, imagex= self.ifPressed )
        self.master.destroy()
        #this automatically destroys the button too