import tkinter
from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.geometry("900x900")
base.resizable(False, False)


class backgound(Frame):
    
    def __init__(self, masterx = base, imagex = "backgroundspookyforest.jpg" ):
        super().__init__(master= masterx)
        self.pack()

        self.picter = Image.open(imagex)
        self.picter = self.picter.resize([900,900])
        tkinterconver = ImageTk.PhotoImage(self.picter)

        self.label = Label(master = self, image= tkinterconver)
        self.label.storage = tkinterconver
        
        self.label.pack(expand= True, fill= "both")

    def kys(self):
        self.destroy()

class scenebutton(Button):

    def __init__(self, ifPressed, locx, locy, masterx = base, textx = "Continue", color = "Grey", widthx = 75, heighty = 25, ):
        super().__init__(master= masterx, text = textx, width= widthx, height= heighty, fg= color, command = self.switchscreen)
        self.masterx = masterx
        self.textx = textx
        self.color = color
        self.ifPressed = ifPressed
        #if pressed is supposed to be an image path to the next scene or something idk
        self.place(anchor= "center", relx = locx, rely = locy )
    
    def switchscreen(self):
        self.ifPressed

        global TheBackground 
        TheBackground = backgound(masterx = base, imagex= self.ifPressed )
        self.master.destroy()
        #this automatically destroys the button too


#scene one
location1 = backgound(masterx= base, imagex= "backgrounddesk.jpg" )
button1 = scenebutton(masterx = location1, textx= "Use laptop", ifPressed= "backgroundlaptop.jpg", locx= .5, locy = .5 )
 


base.mainloop()