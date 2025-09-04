class rectangle:
    def show(self):
        self.height = int(input("Enter you Height:"))
        self.breadth = int(input("Enter your Breadth:"))


    def area(self):
        self.area = self.height * self.breadth
        print("The area is ", self.area)


    def perimeter(self):
        self.perimeter = 2*(self.height + self.breadth)
        print("The perimeter is ", self.perimeter)


if __name__ == '__main__':
    r = rectangle()
    r.show()
    r.area()
    r.perimeter()

