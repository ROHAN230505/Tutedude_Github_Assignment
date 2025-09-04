#from tkinter import  Tk,Label,Entry,Button,END
from tkinter import  *

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Jenekar")
        self.root.wm_geometry("500x500+50+50")

        self.lblname = Label(master=self.root,text="Enter name ",
                                font=('Consolas',18,'bold'))
        self.lblname.place(x = 20,y = 20,width=200,height=30)

        self.enname = Entry(master=self.root,font=('Consolas',18,'bold'))
        self.enname.place(x = 240,y = 20,width=200,height=30)

        self.btnok = Button(master=self.root,text = "OK ",
                            font=('Consolas',18,'bold'),
                            command=self.show)
        self.btnok.place(x=20, y=70, width=100, height=30)

        self.btnclr = Button(master=self.root,text = "clear",
                             font=('Consolas',18,'bold'),command=self.clear)
        self.btnclr.place(x = 140,y = 70,width=100,height=30)

        self.root.mainloop()  # holds the window

    def show(self):
        self.enname.insert(0,"Binary Brains")

    def clear(self):
        self.enname.delete(0,END)


if __name__ == '__main__':
    g = Gui()