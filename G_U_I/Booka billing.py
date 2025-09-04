from tkinter import *
from PIL import Image
from fpdf import FPDF
import pyautogui


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("BOOK BILLING")
        self.root.geometry("500x500+50+50")
        self.root.iconbitmap("C:/Users/Lenovo/Pictures/BOOK_BILLING.ico")
        self.root.config(bg="#96C9F4")

        self.book_name = Label(master=self.root, text="BOOK NAME :", font="Consolas", fg="red", bg="#96C9F4")
        self.book_name.place(x=5,y=10, width = 160, height = 30)
        self.ent_name = Entry(master = self.root, font="Consolas")
        self.ent_name.place(x=200, y=10, width=200, height=30)

        self.book_qunt = Label(master = self.root, text="BOOK QUANTITY :",font="Consolas", fg="red", bg ="#96C9F4")
        self.book_qunt.place(x=5, y=60, width= 160, height=30)
        self.ent_qunt = Entry(master = self.root, font="Consolas")
        self.ent_qunt.place(x=200, y=60, width=200, height=30)

        self.book_price = Label(master = self.root, text="BOOK PRICE :", font="Consolas", fg="red", bg="#96C9F4")
        self.book_price.place(x=5, y=110, width=160, height=30)
        self.ent_price = Entry(master = self.root, font="Consolas")
        self.ent_price.place(x=200, y=110, width=200,height=30)

        self.discount = Label(master =self.root, text="DISCOUNT :", font="Consolas", fg="red", bg="#96C9F4")
        self.discount.place(x=5, y=160, width=160, height=30)
        self.ent_dis = Entry(master=self.root, font="Consolas")
        self.ent_dis.place(x=200, y=160, width=200, height=30)

        self.discount_price = Label(master = self.root, text="DISCOUNT AMOUNT :", font="Consolas", fg="red", bg="#96C9F4")
        self.discount_price.place(x= 5, y=210, width=160, height=30)
        self.ent_dis_prc = Entry(master = self.root, font="Consolas")
        self.ent_dis_prc.place(x=200, y=210, width=200, height=30)

        self.total_amt = Label(master = self.root, text="TOTAL AMOUNT :", font="Consolas", fg="red", bg="#96C9F4")
        self.total_amt.place(x=5, y=260, width = 160)
        self.ent_total_amt = Entry(master = self.root, font = "Consolas")
        self.ent_total_amt.place(x=200, y=260, width=200, height=30)

        self.pay_amt = Label(master = self.root, text="PAYABLE AMOUNT :", font="CONSOLAS", fg="red", bg="#96C9F4")
        self.pay_amt.place(x=5, y=310, width = 160, height = 30)
        self.ent_pay_amt = Entry(master = self.root, font = "Consolas")
        self.ent_pay_amt.place(x= 200, y=310, width = 200, height = 30)

        self.btn_ok = Button(master = self.root, text = "OK", font="Consolas",bg="#96C9F4", command=self.tot)
        self.btn_ok.place(x=40, y=360, width=40, height=30)

        self.btn_prt_bill = Button(master = self.root, text = "PRINT BILL", font="Consolas", bg="#96C9F4", command = self.ptr_bill)
        self.btn_prt_bill.place(x=100, y=360, width = 140, height=30)

        self.btn_clr = Button(master = self.root, text="NEXT ENTRY", font="Consolas",bg="#96C9F4", command=self.clear)
        self.btn_clr.place(x=260, y=360, width=140, height=30)

        self.root.mainloop()

    def tot(self):
        a = int(self.ent_qunt.get())
        b = int(self.ent_price.get())
        c = a*b


        self.ent_total_amt.insert(0, c)

        if (a>=1 and a<=5):
            self.ent_dis.insert(0,"15 %")
            d = 0.15 * c
            self.ent_dis_prc.insert(0, d)
            p = c -d
            self.ent_pay_amt.insert(0, p)


        elif (a>=6 and a<=20):
            self.ent_dis.insert(0,"20 %")
            d = 0.20 * c
            self.ent_dis_prc.insert(0, d)
            p = c - d
            self.ent_pay_amt.insert(0, p)


        elif (a>=20 and a<=50):
            self.ent_dis.insert(0,"30 %")
            d = 0.30 * c
            self.ent_dis_prc.insert(0, d)
            p = c - d
            self.ent_pay_amt.insert(0, p)

        else:
            self.ent_dis.insert(0,"50 %")
            d = 0.50 * c
            self.ent_dis_prc.insert(0, d)
            p = c - d
            self.ent_pay_amt.insert(0, p)



    def clear(self):
        self.ent_name.delete(0,END)
        self.ent_qunt.delete(0,END)
        self.ent_price.delete(0,END)
        self.ent_dis.delete(0,END)
        self.ent_dis_prc.delete(0,END)
        self.ent_total_amt.delete(0,END)
        self.ent_pay_amt.delete(0,END)

    def ptr_bill(self):
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        img = pyautogui.screenshot(region=(x, y, w, h))
        img.save("screenshot.png")

        image_name = "screenshot.png"
        pdf_name = "screenshot.pdf"

        image = Image.open(image_name)
        width, height = image.size

        pdf = FPDF(unit="pt", format=[width, height])
        pdf.add_page()
        pdf.image(image_name, 0, 0)
        pdf.output(pdf_name, "F")

        print("PDF Has been created!")


if __name__ == '__main__':
    g = GUI()
