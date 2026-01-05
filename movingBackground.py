import tkinter
from PIL import Image, ImageTk
from tkinter import *

class backgound(Frame):
    
    def __init__(self, masterx = None, imagex = "backgroundspookyforest.jpg" ):
        super().__init__(master = masterx ,image = imagex)
        self.piwolo = Image.open(imagex)
        self.piwolo = self.piwolo.resize(size="1500x900")
        self.config(imagex = self.piwolo)
