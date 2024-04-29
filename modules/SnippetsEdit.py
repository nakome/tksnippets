from tkinter import *
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import Style

# import StartPage if cancel
from modules import StartPage as s

# import database
from utils.database import database

# Read data from a JSON file
from utils.config import config


class SnippetsEdit(Frame):

    # init class
    def __init__(self, master):

        # init frame
        Frame.__init__(self, master)

        style = Style()

        # get database items by uid
        self.uid = master.uid
        if self.uid:
            data = database().get_by_uid(self.uid)

        self.title = Label(self, text=config["t_title"])
        self.title.grid(row=0, column=0, padx=10, sticky="nw")

        self.entry_title = Entry(self, width=40)
        self.entry_title.insert(END, data[1])
        self.entry_title.grid(row=1, column=0, padx=10, ipady=3, sticky="nw")

        self.description = Label(self, text=config["t_description"])
        self.description.grid(row=2, column=0, padx=10, sticky="nw")

        self.entry_description = Entry(self, width=40)
        self.entry_description.insert(END, data[2])
        self.entry_description.grid(row=3, column=0, padx=10, ipady=3, sticky="nw")

        self.category = Label(self, text=config["t_category"])
        self.category.grid(row=0, column=1, padx=10, sticky="nw")

        self.entry_category = ttk.Combobox(self, values=config["languages"], width=30)
        self.entry_category.set(data[5])
        self.entry_category.grid(row=1, column=1, padx=10, ipady=2, sticky="nw")

        self.date = Label(self, text=config["t_updated"])
        self.date.grid(row=2, column=1, padx=10, sticky="nw")

        self.entry_date = Entry(self, width=33)
        self.entry_date.insert(END, data[4])
        self.entry_date.grid(row=3, column=1, padx=10, ipady=3, sticky="nw")

        self.content = Label(self, text=config["t_content"])
        self.content.grid(row=4, column=0, padx=10, ipady=3, sticky="nw")

        self.entry_content = scrolledtext.ScrolledText(self, width=75, height=20)
        self.entry_content.insert(END, data[3])
        self.entry_content.grid(row=5, columnspan=2, padx=10, sticky="nw")
        self.entry_content.configure(
            background=style.colors.dark,
            foreground=style.colors.light,
            font=("Consolas", 11, "normal"),
        )

        btn = ttk.Button(
            self,
            text=config["btn_save"],
            width=8,
            bootstyle="primary",
            command=lambda: self.update_snippet(),
        )
        btn.grid(row=6, column=0, padx=10, pady=10, sticky="nw")

        btnCancel = ttk.Button(
            self,
            text=config["btn_cancel"],
            width=8,
            bootstyle="warning",
            command=lambda: master.switch(s.StartPage),
        )
        btnCancel.grid(row=6, column=0, padx=80, pady=10, sticky="nw")

        btnDel = ttk.Button(
            self,
            text=config["btn_remove"],
            width=8,
            bootstyle="danger",
            command=lambda: self.remove_snippet(self.entry_title.get()),
        )
        btnDel.grid(row=6, column=1, padx=10, pady=10, sticky="se")

    # update snippet
    def update_snippet(self):
        t = self.entry_title.get()
        if not t:
            Messagebox.show_error(
                message=config["diag_empty_title"], title=config["diag_error"]
            )
        d = self.entry_description.get()
        if not d:
            Messagebox.show_error(
                message=config["diag_empty_description"], title=config["diag_error"]
            )
        c = self.entry_content.get("1.0", END)
        if len(c) < 2:
            Messagebox.show_error(
                message=config["diag_empty_content"], title=config["diag_error"]
            )
        else:

            cc = self.entry_category.get()

            if t and d:
                database().update(self.uid, t, d, c, cc)
                Messagebox.ok(
                    message=config["diag_success_updated"], title=config["diag_success"]
                )
                self.master.switch(s.StartPage)

    # remove snippet
    def remove_snippet(self, title):
        result = Messagebox.okcancel(
            message=config["diag_success_remove"], title=config["diag_remove"]
        )

        if result == "OK" and self.uid:
            database().delete_uid(self.uid)
            self.master.switch(s.StartPage)
