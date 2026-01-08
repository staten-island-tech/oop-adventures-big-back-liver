
import tkinter
from tkinter import *
from PIL import Image, ImageTk

from app import backgound, scenebutton, UselessButton, dialogue

base = Tk()
base.geometry("900x900")
base.resizable(False, False)
specialsring = StringVar()
TheBackground = backgound(masterx = base, imagex= self.ifPressed )
dialgoue1 = dialogue(masterx= TheBackground,textx= "Let's see what my followers are saying. Maybe they could give me some ideas.")

useLaptop2 = scenebutton(identity= "Screen", masterx=TheBackground, textx= "Check Messages", ifPressed="backgroundlaptopScreen.jpg",  locx= .5, locy = .4)