from tkinter import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Rohan Jenekar")
        self.root.iconbitmap("C:/Users/Lenovo/Downloads/poke.ico")  #TO SET AN ICON TO THE WINDOWS
        self.root.state("zoomed")                                   #TO OPEN THE WINDOW ALREADY ZOOMED OUT
        self.root.config(bg="#96C9F4")                            #TO CHANGE THE BACKGROUND COLOR TO SKY BLUE
        
        self.root.geometry("500x500+50+100")
        self.root.mainloop()

if __name__ == '__main__':
    g = GUI()
