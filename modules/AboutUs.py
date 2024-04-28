from tkinter import *
import webbrowser
from tkinter import ttk

# import StartPage if cancel
from modules import StartPage as s


class AboutUs(Frame):

    # init class
    def __init__(self, master):

        # init frame
        Frame.__init__(self, master)

        # label info
        Label(self,text="Version: 1.0.0").pack(padx=10,anchor="w")
        Label(self,text="Developer: Moncho Varela").pack(padx=10,anchor="w")
        Label(self,text="Date: June 10 2019").pack(padx=10,anchor="w")

        self.github = Label(self, text="Github source 🚀", fg="blue", cursor="hand2")
        self.website = Label(self, text="My Website 👩‍🚀", fg="blue", cursor="hand2")

        self.website.bind("<Button-1>",lambda e: self.callback("https://monchovarela.es"))
        self.website.pack(padx=10, anchor="w")

        self.github.bind("<Button-1>",lambda e: self.callback("https://github.com/monchovarela/tksnippets"))
        self.github.pack(padx=10, anchor="w")

        btn = ttk.Button(self, text="Back", width=8, command=lambda: master.switch(s.StartPage) )
        btn.pack(padx=10, pady=10, anchor="w")

    def callback(self, url):
        webbrowser.open_new(url)
