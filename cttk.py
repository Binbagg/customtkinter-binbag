import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()  
app.geometry("400x240")

binbag_image = customtkinter.CTkImage(light_image=Image.open(""),
                                  size=(50, 50))

offbeat_image = customtkinter.CTkImage(light_image=Image.open(""),
                                       size=(50,50))

stunart_image = customtkinter.CTkImage(light_image=Image.open(""),
                                       size=(50,50))


crap = customtkinter.CTkButton(app,text="abinbag", image=binbag_image)
crap.grid(column=1, row=1)
offbeat = customtkinter.CTkButton(app, text="aoffbeat", image=offbeat_image)
offbeat.grid(column=1, row=2)
stunart = customtkinter.CTkButton(app, text="astunart", image=stunart_image)
stunart.grid(column=1, row=3)
app.mainloop()
