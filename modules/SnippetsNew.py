from tkinter import *
from tkinter import font
from tkinter import scrolledtext
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style

# import StartPage if cancel
from modules import StartPage as s

# import database
from utils.database import database


class SnippetsNew(Frame):

    # init class
    def __init__(self, master):

        # init frame
        Frame.__init__(self, master)

        style = Style()

        # Read data from a JSON file
        from utils.config import config

        self.title = Label(self, text="Title")
        self.title.grid(row=0, column=0, padx=10, sticky="nw")

        self.entry_title = Entry(self, width=40)
        self.entry_title.grid(row=1, column=0, padx=10, ipady=3, sticky="nw")

        self.description = Label(self, text="Description")
        self.description.grid(row=2, column=0, padx=10, sticky="nw")

        self.entry_description = Entry(self, width=40)
        self.entry_description.grid(row=3, column=0, padx=10, ipady=3, sticky="nw")

        self.category = Label(self, text="Category")
        self.category.grid(row=0, column=1, padx=10, sticky="nw")

        self.entry_category = ttk.Combobox(self, values=config["languages"], width=30)
        self.entry_category.grid(row=1, column=1, padx=10, ipady=2, sticky="nw")

        self.date = Label(self, text="Created")
        self.date.grid(row=2, column=1, padx=10, sticky="nw")

        self.entry_date = Entry(self, width=33, state="disabled")
        self.entry_date.grid(row=3, column=1, padx=10, ipady=3, sticky="nw")

        self.content = Label(self, text="Snippet")
        self.content.grid(row=4, column=0, padx=10, sticky="nw")

        self.entry_content = scrolledtext.ScrolledText(self, width=75, height=20)
        self.entry_content.grid(row=5, columnspan=2, padx=10, sticky="nw")
        self.entry_content.configure(
            background=style.colors.dark,
            foreground=style.colors.light,
            font=("Consolas", 11, "normal"),
        )

        btn = ttk.Button(
            self,
            text="Save",
            width=8,
            bootstyle="primary",
            command=lambda: self.save_snippet(),
        )
        btn.grid(row=6, column=0, padx=10, pady=10, sticky="nw")

        btnCancel = ttk.Button(
            self,
            text="Cancel",
            width=8,
            bootstyle="danger",
            command=lambda: master.switch(s.StartPage),
        )
        btnCancel.grid(row=6, column=0, padx=80, pady=10, sticky="nw")

    def save_snippet(self):
        t = self.entry_title.get()
        if not t:
            Messagebox.show_error(message="The title is empty", title="Error")
        cc = self.entry_category.get()
        if not cc:
            Messagebox.show_error(message="The category is empty", title="Error")
        d = self.entry_description.get()
        if not d:
            Messagebox.show_error(message="The description is empty", title="Error")
        c = self.entry_content.get("1.0", END)
        if len(c) < 2:
            Messagebox.show_error(message="The content is empty", title="Error")
        else:
            if t and d:
                database().set(t, d, c, cc)
                Messagebox.ok(message="The db was updated", title="Information")
                self.master.switch(s.StartPage)
