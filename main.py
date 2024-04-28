from tkinter import *
from tkinter import ttk

# import sections
from modules.StartPage import StartPage
from modules.SnippetsNew import SnippetsNew
from modules.AboutUs import AboutUs


# main content class
class MainContent(Tk):

    # init class
    def __init__(self):
        # class is a frame
        Tk.__init__(self)

        # title
        self.title("Snippets app")

        # init frame
        self._frame = None

        # uid of database item
        self.uid = IntVar()

        # switch frame on init
        self.switch(StartPage)

    # switch frame method
    def switch(self, frame_class):

        # destroy and replace frame
        new_frame = frame_class(self)

        # destroy frames if not empty
        if self._frame is not None:
            self.uid = False
            self._frame.destroy()

        # create new frame
        self._frame = new_frame

        # create container
        self._frame.pack(side="top", fill="both", expand=True)

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        # create menu
        self.create_menu()

    # create menu
    def create_menu(self):
        menubar = Menu(self)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New snippet", command=lambda: self.switch(SnippetsNew))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Us", command=lambda: self.switch(AboutUs))
        menubar.add_cascade(label="Help", menu=help_menu)

        self.configure(menu=menubar)


if __name__ == "__main__":
    app = MainContent()
    app.resizable(False, False)
    app.mainloop()