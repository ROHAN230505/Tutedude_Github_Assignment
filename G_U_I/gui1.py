from tkinter import Tk

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Rohan Jenekar")
        self.root.geometry("500x500+50+100")
        self.root.mainloop()

if __name__ == '__main__':
    g = GUI()


