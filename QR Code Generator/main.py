import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        #window setup
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='#E7F2F8')

        #customization
        self.title('QR Code Generator')
        self.iconbitmap('empty.ico')
        self.geometry('400x400')


        raw_image = Image.open("./code.png").resize((200,200))
        tk_image = ImageTk.PhotoImage(raw_image)
        self.qr_image = QRImage(self)
        self.qr_image.update_image(tk_image)

        EntryContainer(self)

        #run the app
        self.mainloop()

class EntryContainer(ctk.CTkFrame):
     def __init__(self, parent):
        super().__init__(master=parent, corner_radius=20, fg_color='#74BDCB')
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor='center')
         
        #Grid layout
        self.rowconfigure((0,1), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        #widgets
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.columnconfigure(0, weight=1, uniform='b')
        self.frame.columnconfigure(1, weight=4, uniform='b')
        self.frame.columnconfigure(2, weight=2, uniform='b')
        self.frame.columnconfigure(3, weight=1, uniform='b')
        self.frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.frame, fg_color='white', border_width=0, text_color='black')
        entry.grid(row=0, column=1, sticky='nsew')

        button = ctk.CTkButton(self.frame, text='save')
        button.grid(row=0, column=2, sticky='nsew', padx=10)


class QRImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, 
                         background='red', 
                         bd=0, 
                         highlightthickness=0, 
                         relief='ridge')
        self.place(relx=0.5, rely=0.4, width=200, height=200, anchor='center')

    def update_image(self, image_tk):
        self.create_image(0,0, image=image_tk, anchor='nw')



App()