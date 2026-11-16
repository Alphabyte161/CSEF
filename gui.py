# User interface
import metpy
from tkinter import *
from tkinter import ttk
from functools import partial

# from backend import outputs

def downloadFile():
    print("test")

class WindowApplication(Tk):
    def __init__(self, outputs):
        super().__init__()
        self.outputs = outputs
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

        text1 = Label(frame, text="Enter Date (YYYYMMDD):")
        text1.place(relx=0.02, rely=0.2, anchor='w')
        self.dateBox = Entry(frame, width=20)
        self.dateBox.place(relx=0.395, rely=0.2, anchor='center')
        self.dateBox.bind("<Return>", self.takeInput)

        text2 = Label(frame, text="Select Run Time:")
        text2.place(relx=0.02, rely=0.3, anchor='w')
        self.timeRunOptions = ["00z", "06z", "12z", "18z"]
        self.timeRunCombo = ttk.Combobox(frame, values=self.timeRunOptions, state="readonly")
        self.timeRunCombo.set("Select a Time Run...")
        self.timeRunCombo.place(relx=0.29, rely=0.3, anchor='w')

        text3 = Label(frame, text="Select Member Parameter:")
        text3.place(relx=0.02, rely=0.4, anchor='w')

        self.dataOptions = {"2m Temperature: Min": ("temp", "min"), 
                            "2m Temperature: Max": ("temp", "min"), 
                            "2m Temperature: Mean": ("temp", "min"), 
                            }
        self.combo = ttk.Combobox(frame, values=list(self.dataOptions.keys()), state="readonly")
        self.combo.set("Select a dataset...")
        self.combo.place(relx=0.29, rely=0.4, anchor='w')

        self.combo.bind("<<ComboboxSelected>>", self.onSelect)

    def takeInput(self, event=None):
        dateTextInput = self.dateBox.get()
        print(f"Date entered: {dateTextInput}")

    def downloadFile(self):
        print("test")

    def onSelect(self, event):
        selectedItem = self.combo.get()
        print(f"Selected: '{selectedItem}'")

appSetup = WindowApplication("nil")
appSetup.mainloop()