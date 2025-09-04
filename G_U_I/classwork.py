from tkinter import*
from pymysql import*

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Rohan Jenekar")
        self.root.geometry("500x500+50+100")
        self.root.state("zoomed")

        self.lblrno = Label(master=self.root, text = "Roll no :")
        self.lblrno.place(x = 0, y = 10, width = 100, height = 20 )

        self.enrno = Entry(master=self.root)
        self.enrno.place(x=120, y=10, width=150, height=25)

        self.lblname = Label(master=self.root, text="Name :")
        self.lblname.place(x=0, y=50, width=100, height=20)

        self.enname = Entry(master=self.root)
        self.enname.place(x=120, y=50, width=150, height=25)

        self.lblcour = Label(master=self.root, text="Course :")
        self.lblcour.place(x=0, y=100, width=100, height=20)

        self.encour = Entry(master=self.root)
        self.encour.place(x=120, y=100, width=150, height=25)

        self.lblfee = Label(master=self.root, text="Fees :")
        self.lblfee.place(x=0, y=150, width=100, height=20)

        self.enfee = Entry(master=self.root)
        self.enfee.place(x=120, y=150, width=150, height=25)

        self.btnok =  Button(master = self.root, text = "FIRST")
        self.btnok.place(x = 5, y = 200, width = 90, height = 40, command = self.first())

        self.btnnxt = Button(master =  self.root, text = "NEXT",command = self.next)
        self.btnnxt.place(x = 100, y = 200, width = 90, height = 40,)

        self.btnprev = Button(master =  self.root, text = "PREV")
        self.btnprev.place(x = 200, y = 200, width = 90, height = 40, command = self.previous())

        self.btnlst = Button(master =  self.root, text = "LAST")
        self.btnlst.place(x = 300, y = 200, width = 90, height = 40, command = self.last())

        self.btnnew = Button(master =  self.root, text = "NEW")
        self.btnnew.place(x = 5, y = 250, width = 90, height = 40, command = self.new())

        self.btnins = Button(master =  self.root, text = "INSERT")
        self.btnins.place(x = 100, y = 250, width = 90, height = 40, command = self.insert())

        self.btnupd = Button(master =  self.root, text = "UPDATE")
        self.btnupd.place(x = 200, y = 250, width = 90, height = 40, command = self.update())

        self.btndel = Button(master = self.root, text = "DELETE")
        self.btndel.place(x = 300, y = 250, width = 90, height = 40, command = self.delete())

        self.connectToDB()
        self.root.mainloop()

    def connectToDB(self):
        # Connection string
        self.conn = connect(host="localhost",
                            db="studendb",
                            user="root",
                            password="889713724Rkj@123",
                            port=3306)

        self.cur = self.conn.cursor()

        self.cur.execute("select * from studen")

        self.data = self.cur.fetchall()

        self.enrno.insert(0, self.data[0][0])
        self.enname.insert(0, self.data[0][1])
        self.encour.insert(0, self.data[0][2])
        self.enfee.insert(0, self.data[0][3])

    def first(self):
        pass

    def next(self):
        self.enrno.delete(0,END)
        self.enname.delete(0,END)
        self.encour.delete(0,END)
        self.enfee.delete(0,END)

        self.enrno.insert(0, self.data[1][0])
        self.enname.insert(0, self.data[1][1])
        self.encour.insert(0, self.data[1][2])
        self.enfee.insert(0, self.data[1][3])
    def previous(self):
        pass

    def last(self):
        pass

    def new(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    g = GUI()


