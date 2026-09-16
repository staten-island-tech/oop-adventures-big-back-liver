
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import time

import pygame
pygame.init()
pygame.mixer.init()

def notificationSFX():
    sfxdomer = pygame.mixer.Sound("audio file\DOMER.mp3")
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sfxdomer)
    base.update()
    time.sleep(2)  
    base.update()

def useDialogue(text, espeed = 50, file = "portrait/HamsterDefault.jpg"):
    dialgoue = dialogue(masterx= TheBackground, textx= text, speed= espeed, portraitfile= file )


base = Tk()
base.geometry("900x900")
base.resizable(False, False)
specialsring = StringVar() #the identity of a button will change this


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
        self.lower()
        base.update()


    def kys(self):
        self.destroy()
        


class scenebutton(Button):

    def __init__(self, ifPressed, locx, locy, identity, masterx, textx = "Continue", fgcolor = "Grey", bgcolor = "Black" ):
        super().__init__(master= masterx, text = textx, width= 15, height= 2, fg= fgcolor, bg= bgcolor, command = self.switchscreen)
        self.masterx = masterx
        self.textx = textx
        self.ifPressed = ifPressed
        self.identity = identity      
        #if pressed is supposed to be an image path to the next scene or something idk
        self.place(anchor= "center", relx = locx, rely = locy )
        self.lift()
        #loc is a float that hsdjfghgfrsjhhfrujfdhg
         
    def switchscreen(self):
        
        specialsring.set(self.identity)
        print(specialsring)
        print(self.identity)

        global TheBackground 
        TheBackground = backgound(masterx = base, imagex= self.ifPressed )
        self.master.destroy()
        #this automatically destroys the button too

    
class dialogue(Label):

    def __init__(self,  textx, masterx, fgcolor = "Grey", bgcolor = "Black", speed = 50, portraitfile = "portrait/HappyHamster.jpg" ):


        super().__init__(master= masterx, wraplength= 600, fg = fgcolor, bg= bgcolor, font = ("Arial", 20))
        
        
        #label
        self.place(anchor= "s", relx = .5, rely = .9,  )
        for wig in TheBackground.winfo_children():
            if wig.winfo_class() == "Button":
                wig.config(state = 'disabled') 
        TheBackground.update()

        #hahahhaha i got this effect to  work 
        b =""
        for char in textx:
            self.after(ms=speed)
            self.update()
            b = b + char
            self.config(text= b)

        global button_pressedok    
        button_pressedok = StringVar()
        ok = Button(master= TheBackground, text= "Next", fg = "grey", bg = "black", command=lambda: button_pressedok.set(value="buttonpressedok"))
        ok.place(anchor="n", relx=.5, rely = .9)

        #pause

        base.wait_variable(button_pressedok)
        for wig in TheBackground.winfo_children():
            wig.config(state = 'normal')
        #returning
        TheBackground.update()
        ok.destroy()
        self.destroy()
        

class UselessButton(Button):

    def __init__(self, locx, locy, message, masterx, textx = "Continue", fgcolor = "Grey", bgcolor = "Black"):
        
        super().__init__(master= masterx, text = textx, width= 15, height= 2, fg= fgcolor, bg= bgcolor, command = self.Press )
        self.masterx = masterx
        self.textx = textx
        self.message = message
        self.place(anchor= "center", relx = locx, rely = locy )
         

    def Press(self):
        self.dialogue = dialogue(masterx=TheBackground, textx= self.message)


#testing hallway

TheBackground = backgound(masterx= base, imagex= "backgroundlaptop.jpg")
useDialogue("i hate my life.")

useDialogue("That was so weird. I hope nothing bad happens.")
TheBackground.kys() 
TheBackground = backgound(masterx= base, imagex= "backgrounddesk.jpg")
UseLaptop2 = UselessButton(masterx = TheBackground, textx= "Use laptop", locx= .4, locy = .6, message= "no thanks...")
LeaveRoom2 = scenebutton(masterx= TheBackground, identity= "LeaveRoom", textx= "Leave Room", locx= .7, locy=.5, ifPressed= "backgroundhallway.jpg")
base.wait_variable(specialsring)

#Knocking sound (will add later)

#allows user to explore:

#create rooms buttons here

#hallway
print(specialsring)
ExitHall = scenebutton(masterx= TheBackground, identity= "ExitHall", textx= "Exit Hallway", locx= .4, locy=.4, ifPressed= "backgroundhallway.jpg")
Bathroom = scenebutton(masterx= TheBackground, identity= "Bathroom", textx= "Bathroom", locx= .55, locy=.6, ifPressed= "bathroom.png.jpg")
if specialsring == "LeaveRoom":

    ExitHall = scenebutton(masterx= TheBackground, identity= "ExitHall", textx= "Exit Hallway", locx= .4, locy=.4, ifPressed= "backgroundhallway.jpg")
    Bathroom = scenebutton(masterx= TheBackground, identity= "Bathroom", textx= "Bathroom", locx= .55, locy=.6, ifPressed= "bathroom.png.jpg")

    TheBackground.kys() 
    TheBackground = backgound(masterx= base, imagex= "backgroundhallway.jpg")
base.mainloop()
