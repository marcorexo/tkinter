import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        #window setup
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='#E7F2F8')

        #customization
        self.title('')
        self.iconbitmap('empty.ico')
        self.geometry('400x400')

        EntryContainer(self)

        #run the app
        self.mainloop()

class EntryContainer(ctk.CTkFrame):
     def __init__(self, parent):
         super().__init__(master=parent, corner_radius=20, fg_color='#74BDCB')
         self.place(relx=0.5, rely=1, relwidth=1, relheight=0.5, anchor='center')



App()