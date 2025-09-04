class calculator:
    def read(self):
        self.num1 = int(input("ENTER YOUR FIRST NO."))
        self.num2 =  int(input("ENTER YOUR SECONND NUMBER"))

    def add(self):
        self.add = self.num1 + self.num2
        print("THE ADDITION is ",self.add)

    def sub(self):
        self.sub = self.num1 - self.num2
        print("The Subtraction is",self.sub)


if __name__ == '__main__':
    c = calculator()
    c.read()
    c.add()
    c.sub()