import sys
import subprocess

def downloadlibs():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'customtkinter', 'Pillow'])


#downloablibs()                            REMOVE START HASHTAG TO DOWNLOAD REQUIRED LIBRARIES ON CODE RUN


import tkinter
import customtkinter
import os
import sys
from PIL import Image
from pathlib import Path





customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()  
app.geometry("400x240")


location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) #locates working directory to use images


binbag_image = customtkinter.CTkImage(light_image=Image.open( location + "\\acrap.png"),
                                  size=(50, 50))

offbeat_image = customtkinter.CTkImage(light_image=Image.open( location + "\\aoffbeat.png"),
                                       size=(50,50))

stunart_image = customtkinter.CTkImage(light_image=Image.open( location + "\\astunart.png"),
                                       size=(50,50))



crap = customtkinter.CTkButton(app,text="abinbag", image=binbag_image)
crap.grid(column=1, row=1)
offbeat = customtkinter.CTkButton(app, text="aoffbeat", image=offbeat_image)
offbeat.grid(column=1, row=2)
stunart = customtkinter.CTkButton(app, text="astunart", image=stunart_image)
stunart.grid(column=1, row=3)
app.mainloop()
