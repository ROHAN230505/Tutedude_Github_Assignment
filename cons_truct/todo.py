class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def getarea(self)->float:
        area = self.length * self.breadth
        return area
    def getperi(self)->float:
        perimeter = 2 * (self.length + self.breadth)
        return perimeter

if __name__ == "__main__":
    length = int(input("ENTER THE LENGTH :"))
    breadth = int(input("ENTER THE BREADTH :"))
    r = Rectangle(length, breadth)
    print("THE AREA IS :",r.getarea())
    print("THE PERIMETER IS :",r.getperi())

