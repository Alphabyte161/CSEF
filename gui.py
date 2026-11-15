# User interface
import metpy
from tkinter import *
from tkinter import ttk
from functools import partial

from backend import outputs

def downloadFile():
    print("test")

class WindowApplication(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('550x300')
        self.title("CSEF Viewer")

        menubar = Menu(self)
        self.config(menu=menubar)
        menubar.add_command(label="Exit", command=self.destroy)
        menubar.add_command(label="Download", command=self.downloadFile)

        frame = Frame(self, width=550, height=300)
        frame.pack(fill="both", expand=True)
        
        title = Label(frame, text="CSEF Window Viewer - v.0.0.1")
        title.place(relx=0.5, rely=0.05, anchor='n')

        text1 = Label(frame, text="Select Member Parameter:")
        text1.place(relx=0.02, rely=0.15, anchor='w')

        dataOptions = ["2m Temperature: Min", "2m Temperature: Max", "2m Temperature: Mean", "2m Dewpoint: Mean"]
        self.combo = ttk.Combobox(frame, values=dataOptions, state="readonly")
        self.combo.set("Select a dataset...")
        self.combo.place(relx=0.075, rely=0.25, anchor='w')

        self.combo.bind("<<ComboboxSelected>>", self.onSelect)

    def downloadFile(self):
        print("test")

    def onSelect(self, event):
        selectedItem = self.combo.get()
        print(f"Selected: '{selectedItem}'")

appSetup = WindowApplication()
appSetup.mainloop()