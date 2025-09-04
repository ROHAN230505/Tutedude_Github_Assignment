from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, length, breadth, radius):
        self.length = length
        self.breadth = breadth
        self.radius = radius

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def area(self):
        area = self.length * self.breadth
        print("Area:", area)

    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        print("Perimeter:", perimeter)


class Circle(Shape):
    def area(self):
        area = 3.14 * (self.radius * self.radius)
        print("Area", area)

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print("Perimeter:", perimeter)


if __name__ == '__main__':
    ch = int(input("Enter your choice :\n 1.Rectangle \n 2.Circle "))
    match ch:
        case 1:
            length = int(input("Enter the Length"))
            breadth = int(input("Enter your breadth:"))
            radius = 0

            r = Rectangle(length, breadth, radius)
            r.area()
            r.perimeter()

        case 2:
            radius = int(input("Enter your Radius :"))
            length = 0
            breadth = 0
            c = Circle(length, breadth, radius)
            c.area()
            c.perimeter()
