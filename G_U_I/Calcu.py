from tkinter import*

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("CALCULATOR")
        self.root.geometry("300x200+50+50")

        self.num1 = Entry(master = self.root, font=("Consolas",30,"bold"))
        self.num1.place(x=10, y=10, width=80, height=30)

        self.num2 = Entry(master = self.root, font=("Consolas",30,"bold"))
        self.num2.place(x=100, y=10, width=80, height=30)

        self.eq = Label(master =self.root,text="=", font=("Consolas",20,"bold"))
        self.eq.place(x=185, y=10, width=10, height=32)


        self.num3 = Entry(master = self.root, font=("Consolas",30,"bold"))
        self.num3.place(x=200, y=10, width=80, height=30)

        self.add = Button(master = self.root,text="+", font=("Consolas",30,"bold"), command = self.add)
        self.add.place(x=10, y=50, width=50, height=50)

        self.sub = Button(master = self.root, text = "-", font=("Consolas",30,"bold"), command = self.sub)
        self.sub.place(x=80, y=50, width=50, height=50)

        self.mul = Button(master = self.root, text="X", font=("Consolas",30,"bold"), command = self.mul)
        self.mul.place(x=150, y=50, width=50, height=50)

        self.div = Button(master = self.root, text="÷", font=("Consolas",30,"bold"), command = self.div)
        self.div.place(x=220, y=50, width=50, height=50)

        self.clear = Button (master = self.root, text="CLEAR", font=("Consolas",17,"bold"), command = self.clear)
        self.clear.place(x=100, y=130 ,width=70, height=50)

        self.root.mainloop()

    def add(self):
        a = int(self.num1.get())
        b = int(self.num2.get())

        c = a + b
        self.num3.insert(0,c)

    def sub(self):
        a = int(self.num1.get())
        b = int(self.num2.get())

        c = a - b
        self.num3.insert(0,c)

    def div(self):
        a = int(self.num1.get())
        b = int(self.num2.get())

        c = a / b
        self.num3.insert(0,c)

    def mul(self):
        a = int(self.num1.get())
        b = int(self.num2.get())

        c = a * b
        self.num3.insert(0,c)

    def clear(self):
        self.num1.delete(0,END)
        self.num2.delete(0,END)
        self.num3.delete(0,END)

if __name__ == '__main__':
    g = GUI()