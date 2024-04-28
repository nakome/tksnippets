from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style

# import sections snippets
from modules.SnippetsEdit import SnippetsEdit

# import database
from utils.database import database

# import custom enty with placeholder
from utils.placeholder import EntryWithPlaceholder


class StartPage(Frame):

    # init class
    def __init__(self, master):
        # frame
        Frame.__init__(self, master)

        self.master = master

        self.e = EntryWithPlaceholder(self, "Search")
        self.e.pack(side="top", fill="x", ipady=5, ipadx=5)
        self.e.bind("<KeyPress>", self.search_by_title)

        # Add some style:
        style = Style()

        style.configure(
            "Treeview.Heading",
            background=style.colors.dark,
            foreground=style.colors.light
        )

        style.configure(
            "Treeview",
            background=style.colors.light,
            font=("Helvetica", 10, "normal"),
            rowheight=33,
        )

        style.map("Treeview", background=[("selected", style.colors.primary)])

        # create treeview like table
        self.tree = ttk.Treeview(
            self, height=13, columns=("uid", "title", "description", "date", "category")
        )
        self.tree["show"] = "headings"
        self.tree.heading("uid", text="Uid")
        self.tree.column("uid", width=40)
        self.tree.heading("title", text="Title")
        self.tree.column("title", width=120)
        self.tree.heading("description", text="Description")
        self.tree.column("description", width=150)
        self.tree.heading("date", text="Created")
        self.tree.column("date", width=100)
        self.tree.heading("category", text="Category")
        self.tree.column("category", width=100)

        # insert database items
        for item in database().get_all():
            self.tree.insert(
                "", "end", values=(item[0], item[1], item[2], item[4], item[5])
            )

        # Style odd and even rows like table-striped
        self.tree.tag_configure("odd_row", background=style.colors.secondary)
        self.tree.tag_configure("even_row", background=style.colors.light)

        for i in range(self.tree.get_children().__len__()):
            if i % 2 == 0:
                self.tree.item(self.tree.get_children()[i], tags=("even_row",))
            else:
                self.tree.item(self.tree.get_children()[i], tags=("odd_row",))

        self.tree.bind("<Double-1>", self.itemEvent)
        self.tree.pack()

    # search title
    def search_by_title(self, event):
        if event.char == "\r":
            if len(self.e.get()) > 2:
                title = self.e.get()
                # clear tree
                for i in self.tree.get_children():
                    self.tree.delete(i)
                # insert data
                for item in database().find_by_title(title):
                    self.tree.insert(
                        "", "end", values=(item[0], item[1], item[2], item[4], item[5])
                    )
            else:
                # clear tree
                for i in self.tree.get_children():
                    self.tree.delete(i)
                # insert data
                for item in database().get_all():
                    self.tree.insert(
                        "", "end", values=(item[0], item[1], item[2], item[4], item[5])
                    )

    # on double click run method
    def itemEvent(self, event):
        # get selection
        for item in self.tree.selection():
            # get values
            data = self.tree.item(item, "values")
            # get and save on master uid
            self.master.uid = int(data[0])
            # change frame to snippets
            self.master.switch(SnippetsEdit)
