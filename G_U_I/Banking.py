from tkinter import *
from pymysql import*

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("BANKING LOGIN PAGE")
        self.root.geometry("500x500+50+50")
        self.root.iconbitmap("C:/Users/Lenovo/Downloads/BANKING.ico")
        self.root.config(bg="#77b5fe")

        self.custid = Label(master = self.root, text = "CUSTOMER ID:", font=("Times New Roman",10,"bold"), bg="#77b5fe")
        self.custid.place(x=10, y=10, height=40, width=100)
        self.custid_en = Entry(master = self.root, font="Consolas")
        self.custid_en.place(x=120, y=10, height= 30, width=300)

        self.name = Label(master=self.root, text="NAME :", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.name.place(x=10, y=55, height=40, width=100)
        self.name_en = Entry(master = self.root, font = "Consolas")
        self.name_en.place(x=120, y=55, height = 30, width= 300)

        self.mobile = Label(master=self.root, text="MOBILE :", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.mobile.place(x=10, y=100, height=40, width=100)
        self.mobile_en = Entry(master=self.root, font="Consolas")
        self.mobile_en.place(x=120, y=100, height=30, width=300)

        self.acctype = Label(master=self.root, text="ACCOUNT TYPE:", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.acctype.place(x=10, y=150, height=40, width=100)
        self.OPTIONS = [
            "CURRENT",
            "SAVING"
        ]  # etc

        master = self.root

        self.variable = StringVar(master)
        self.variable.set("Select your Account type")  # default value
        self.acctype_menu = OptionMenu(master, self.variable, *self.OPTIONS)
        self.acctype_menu.place(x=120, y=150, height=30, width=300)

        self.gender = Label(master = self.root, text="GENDER",font=("Times New Romman", 10, "bold"), bg="#77b5fe")
        self.gender.place(x=10, y=200, height=40, width=100)
        self.gender_var = IntVar()
        self.male = Radiobutton(master=self.root, text="MALE", variable=self.gender_var, value=1, bg="#77b5fe")
        self.male.place(x=120, y=200, height=40, width=50)
        self.female = Radiobutton(master=self.root, text="FEMALE", variable=self.gender_var, value=2, bg="#77b5fe")
        self.female.place(x=250, y=200, height=40, width=60)

        self.street = Label(master=self.root, text="STREET:", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.street.place(x=10, y=250, height=40, width=100)
        self.street_en = Entry(master = self.root,font="Consolas")
        self.street_en.place(x=120, y=250, height=30, width=300)

        self.city = Label(master=self.root, text="CITY:", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.city.place(x=10, y=300, height=40, width=100)
        self.city_en = Entry(master=self.root, font="Consolas")
        self.city_en.place(x=120 ,y=300 ,height=30, width=300)

        self.state = Label(master=self.root, text="STATE:", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.state.place(x=10, y=350, height=40, width=100)
        self.OPTION = [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Goa",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttarakhand",
            "Uttar Pradesh",
            "West Bengal",
            "Andaman and Nicobar Islands",
            ]
        master = self.root

        self.variable1 = StringVar(master)
        self.variable1.set("SELECT YOUR STATE")  # default value
        self.state_menu = OptionMenu(master, self.variable1, *self.OPTION)
        self.state_menu.place(x=120, y=350, height=30, width=300)

        self.pin = Label(master=self.root, text="PIN CODE:", font=("Times New Roman", 10, "bold"), bg="#77b5fe")
        self.pin.place(x=10, y=400, height=40, width=100)
        self.pin_en = Entry(master= self.root, font="Consolas")
        self.pin_en.place(x=120, y=400, height=30, width=300)

        self.btn_ok = Button(master=self.root, text="OK", font="Consolas", bg="#96C9F4")
        self.btn_ok.place(x=20, y=450, width=80, height=30)

        self.btn_clr = Button(master=self.root, text="CLEAR", font="Consolas", bg="#96C9F4", command=self.CLEAR)
        self.btn_clr.place(x=130, y=450, width=100, height=30)

        self.connectToDB()
        self.root.mainloop()

    def connectTODB(self):
        # Connection string
        self.conn = connect(host="localhost",
                            db="Bank",
                            user="root",
                            password="889713724Rkj@123",
                            port=3306)

        self.cur = self.conn.cursor()

        self.cur.execute("select * from Banktb")


    def OK(self):
        pass

    def CLEAR(self):
        self.custid_en.delete(0,END)
        self.name_en.delete(0,END)
        self.mobile_en.delete(0,END)
        self.street_en.delete(0,END)
        self.city_en.delete(0,END)
        self.pin_en.delete(0,END)
        self.variable.set("Select your account type")
        self.variable1.set("SELECT YOUR STATE")



if __name__ =='__main__':
    g = GUI()
