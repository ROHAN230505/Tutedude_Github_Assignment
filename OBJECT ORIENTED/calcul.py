class calcu:
    def setData(self, n1, n2):
        self.a = n1
        self.b = n2

    def getadd(self) -> int:
        c = self.a +self.b
        return c


if __name__ == '__main__':
    n1 = int(input("Enter your first no. :"))
    n2 = int(input("Enter your second no. :"))
    ca = calcu()
    ca.setData(n1, n2)
    c = ca.getadd()
    print("The addition is", c)