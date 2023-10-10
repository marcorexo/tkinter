import tkinter as tk
from tkinter import ttk

def convert():
    km = entry_val.get() * 1.60934
    output_string.set(km)
    #entryVal = km
    

window  = tk.Tk()
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(window, text='Miles to Kilomters', font='Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_val = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_val)
button = ttk.Button(master=input_frame, text='Convert', command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(master=window, 
                         text='output...', 
                         font='Calibri 24', 
                         textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()