from abc import ABC,abstractmethod
class Fruit(ABC):

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def vitamin(self):
        pass


class Mango(Fruit):

    def color(self):
        print("yellow")

    def taste(self):
        print("Sweet")

    def vitamin(self):
        print("C")



class Orange(Fruit):

    def color(self):
        print("Orange")

    def taste(self):
        print("sour")

    def vitamin(self):
        print("A and C")




if __name__ == '__main__':
	print("Enter Fruit Type")
	s = input()  # "Orange"

	#Converting string into class name using globals() function
	classname = globals()[s]

	obj = classname()
	obj.color()
	obj.taste()
	obj.vitamin()
