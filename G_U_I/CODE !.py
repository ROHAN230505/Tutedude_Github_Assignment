from tkinter import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("LOGIN PAGE")
        self.root.geometry("500x500+50+50")
        self.root.iconbitmap("C:/Users/Lenovo/Downloads/poke.ico")

        self.name = Label(master=self.root, text="NAME :")
        self.name.place(x=10, y=20, width=80, height=40)

        self.enname = Entry(master=self.root, font=("Consolas"))
        self.enname.place(x=100, y=20, width=200, height=30)

        self.passw = Label(master=self.root, text="PASSWORD")
        self.passw.place(x=10, y=60,width=80, height=40)

        self.enpassw = Entry(master=self.root,font=(10), show="*")
        self.enpassw.place(x=100, y=60, width=200, height=30)

        self.check_button1 = Checkbutton(text="C++")
        self.check_button1.place(x=20, y=100, width=80, height= 40)

        self.check_button2 = Checkbutton(text="C")
        self.check_button2.place(x=12, y=130, width=80, height=40)

        self.check_button3 = Checkbutton(text="Pyhton")
        self.check_button3.place(x=25, y=160, width= 80, height=40)

        self.check_button4 = Checkbutton(text="JAVA")
        self.check_button4.place(x=20, y=190, width= 80, height=40)

        self.radio = Radiobutton(master=self.root, text="Male",value=1)
        self.radio.place(x=100, y=100, width=80, height=40)

        self.radio1 = Radiobutton(master=self.root, text="Female",value=0)
        self.radio1.place(x=100, y=130, width=80, height=40)

        self.submit = Button(master=self.root, text="SUBMIT")
        self.submit.place(x=250, y=300, width= 50, height=40)


        self.root.mainloop()


if __name__ == '__main__':
    g = GUI()
