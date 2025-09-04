from tkinter import*
from tkinter import PhotoImage


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("ROHAN")
        self.root.state("zoomed")
        self.image = Image.open("C:/Users/Lenovo/Downloads/poke_trainer_three_star_icon-icons.com_67512.png")
        self.image1 = ImageTk.PhotoImage(image)
        self.Lable1(win, image = self.image1).place(x=0,y=0)
        self.root.mainloop()

if __name__ == '__main__':
    g = GUI()
