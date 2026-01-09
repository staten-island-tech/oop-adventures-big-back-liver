
import tkinter
from tkinter import *
from PIL import Image, ImageTk

import pygame
import time

pygame.init()
pygame.mixer.init()

def notificationSFX():
    sfxdomer = pygame.mixer.Sound("audio file\DOMER.mp3")
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sfxdomer)
    base.update()
    time.sleep(2)  
    base.update()

 
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


class scenebutton(Button):

    def __init__(self, ifPressed, locx, locy, identity, masterx = base, textx = "Continue", fgcolor = "Grey", bgcolor = "Black" ):
        super().__init__(master= masterx, text = textx, width= 15, height= 2, fg= fgcolor, bg= bgcolor, command = self.switchscreen)
        self.masterx = masterx
        self.textx = textx
        self.ifPressed = ifPressed
        self.identity = identity      
        #if pressed is supposed to be an image path to the next scene or something idk
        self.place(anchor= "center", relx = locx, rely = locy )
        #loc is a float that hsdjfghgfrsjhhfrujfdhg
    
    def switchscreen(self):
        self.master.destroy()
        specialsring.set(self.identity)

        global TheBackground 
        TheBackground = backgound(masterx = base, imagex= self.ifPressed )
        
        #this automatically destroys the button too

    
class dialogue(Label):

    def __init__(self,  textx, masterx, fgcolor = "Grey", bgcolor = "Black"):

        super().__init__(master= masterx, wraplength= 600, fg = fgcolor, bg= bgcolor, font = ("Arial", 20))
        self.place(anchor= "s", relx = .5, rely = .9,  )

        #hahahhaha i got this effect to  work 
        b =""
        for char in textx:
            self.after(50)
            self.update()
            b = b + char
            self.config(text= b)
            
        button_pressedok = StringVar()
        ok = Button(master= TheBackground, text= "Next", fg = "grey", bg = "black", command=lambda: button_pressedok.set(value="buttonpressedok"))
        ok.place(anchor="n", relx=.5, rely = .9)
        TheBackground.wait_variable(button_pressedok)
        self.destroy()
        ok.destroy()
        

class UselessButton(Button):

    def __init__(self, locx, locy, message, masterx, textx = "Continue", fgcolor = "Grey", bgcolor = "Black"):
        
        super().__init__(master= masterx, text = textx, width= 15, height= 2, fg= fgcolor, bg= bgcolor, command = self.Press )
        self.masterx = masterx
        self.textx = textx
        self.message = message
        self.place(anchor= "center", relx = locx, rely = locy )

    def Press(self):
        self.dialogue = dialogue(masterx=TheBackground, textx= self.message)
#states from laptop accesss
TheBackground = backgound(base, "backgroundlaptop.jpg")
dialgoue2a = dialogue(masterx= TheBackground,textx= "Let's see what my followers are saying. Maybe they could give me some ideas.")

useLaptop2 = scenebutton(identity= "Screen", masterx= TheBackground, textx= "Check Messages", ifPressed="backgroundlaptopScreen.jpg",  locx= .5, locy = .4)
base.wait_variable(specialsring)
base.update()
TheBackground.update()
notificationSFX()
dialgoue2a = dialogue(masterx= TheBackground, textx= "What was that notification?" )
TheBackground.kys()
TheBackground = backgound(masterx= base, imagex= "backgroundlaptopScreenN1.jpeg")
notificationSFX()
TheBackground.kys() 
TheBackground = backgound(masterx= base, imagex= "backgroundlaptopScreenN2.png")
base.update()
time.sleep(2)
base.update()
dialgoue2a = dialogue(masterx= TheBackground, textx= ".....")
base.mainloop()
