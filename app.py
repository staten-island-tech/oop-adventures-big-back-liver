
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

def useDialogue(text, espeed = 50):
    dialgoue = dialogue(masterx= TheBackground, textx= text, speed= espeed )
base = Tk()
base.geometry("900x900")
base.resizable(False, True)
specialsring = StringVar()


class backgound(Frame):
    
    def __init__(self, masterx = base, imagex = "backgroundbedroom.jpg" ):
        super().__init__(master= masterx)
        self.pack()

        self.picter = Image.open( "background\\" + imagex)
        self.picter = self.picter.resize([900,900])
        tkinterconver = ImageTk.PhotoImage(self.picter)

        self.label = Label(master = self, image= tkinterconver)
        self.label.storage = tkinterconver
        
        self.label.pack(expand= True, fill= "both")

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

    def __init__(self,  textx, masterx, fgcolor = "Grey", bgcolor = "Black", speed = 50):

        super().__init__(master= masterx, wraplength= 600, fg = fgcolor, bg= bgcolor, font = ("Arial", 20))
        self.place(anchor= "s", relx = .5, rely = .9,  )

        #hahahhaha i got this effect to  work 
        b =""
        for char in textx:
            self.after(ms=speed)
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

#scene one
location1 = backgound(masterx= base, imagex= "backgroundbedroom.jpg")
Deskbutton = scenebutton(identity="Deskbutton", masterx= location1, textx = "Go to Desk", ifPressed= "backgrounddesk.jpg", locx= 0.35, locy=0.5 )
LeaveRoom = scenebutton(identity="Leaveroom", masterx= location1, textx= "Leave room", ifPressed= "backgroundhallway.jpg", locx= .7, locy=.5)
base.wait_variable(specialsring)

#scene 2a
if specialsring.get() == "Deskbutton":
    useDialogue( "I'm running out of money....")
    useDialogue("I should probably do a live stream. It's a quick way to get money... ")
    UseLaptop1 = scenebutton(identity= "UseLaptop", masterx = TheBackground, textx= "Use laptop", ifPressed= "backgroundlaptop.jpg", locx= .4, locy = .6 )
    LeaveDesk1 = UselessButton( masterx = TheBackground, textx= "Leave desk", locx= .5, locy = 0.9, message= "I should probably work..." )
    #No. LeaveDesk1 = scenebutton(identity= "LeaveDesk(bedroom)", masterx = TheBackground, textx= "Leave desk", ifPressed= "backgroundbedroom.jpg", locx= .5, locy = 0.9 )
    
    base.wait_variable(specialsring)
    useDialogue( "Let's see what my followers are saying. Maybe they could give me some ideas.")

    useLaptop2 = scenebutton(identity= "Screen", masterx=TheBackground, textx= "Check Messages", ifPressed="backgroundlaptopScreen.jpg",  locx= .5, locy = .4)
    base.wait_variable(specialsring)
    base.update()
    TheBackground.update()
    notificationSFX()
    useDialogue("What was that notification?" )
    TheBackground.kys()
    TheBackground = backgound(masterx= base, imagex= "backgroundlaptopScreenN1.jpeg")
    notificationSFX()
    TheBackground.kys() 
    TheBackground = backgound(masterx= base, imagex= "backgroundlaptopScreenN2.png")
    base.update()
    time.sleep(2)
    base.update()
    useDialogue(text= ".....", espeed= 500)
    notificationSFX()
    TheBackground.kys() 
    TheBackground = backgound(masterx= base, imagex= "LaptopChat.jpeg")
    
    useDialogue("what.... what do i do....", espeed= 200)

    yesRespond = scenebutton(identity= "YESFEET", textx= "Yes", ifPressed= )
    noRespond = scenebutton(identity= "fuhno", textx= "No", ifPressed= )


    if specialsring.get() == "YESFEET":
        useDialogue("um...")
        useDialogue("i mean.... i need some money...")

    #scene 3a




base.mainloop()