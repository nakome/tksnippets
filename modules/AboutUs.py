from tkinter import *
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap import Style

# import StartPage if cancel
from modules import StartPage as s

# Read data from a JSON file
from utils.config import config


class AboutUs(Frame):

    # init class
    def __init__(self, master):

        # init frame
        Frame.__init__(self, master)

        style = Style()

        # label info
        self.txt = Label(self, text=config["about_txt"])
        self.txt.configure(
            width=60,
            height=10,
            font=("Helvetica", 10, "bold"),
            fg=style.colors.light,
            bg=style.colors.dark,
        )
        self.txt.pack(anchor="w")

        self.github = Label(self, text=config["link_txt_1"])
        self.github.configure(fg=style.colors.primary, cursor="hand2")
        self.website = Label(self, text=config["link_txt_2"])
        self.website.configure(fg=style.colors.primary, cursor="hand2")

        self.website.bind("<Button-1>", lambda e: self.callback(config["link_href_2"]))
        self.website.pack(padx=10, anchor="w")

        self.github.bind(
            "<Button-1>",
            lambda e: self.callback(config["link_href_1"]),
        )
        self.github.pack(padx=10, anchor="w")

        btn = ttk.Button(
            self,
            text=config["btn_back"],
            width=8,
            command=lambda: master.switch(s.StartPage),
        )
        btn.pack(padx=10, pady=10, anchor="w")

    def callback(self, url):
        webbrowser.open_new(url)
