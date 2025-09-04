class Person:

    def readperson(self):
        self.name = str(input("Enter your name : "))
        self.age = int(input("Enter your Age : "))

    def showperson(self):
        print("Your name is :", self.name)
        print("Your age is : ", self.age)


class Department:

    def readdept(self):
        self.depart = str(input("Enter your department :"))
        self.dept_no = int(input("Enter your Department no. :"))

    def showdept(self):
        print("Your Department is", self.depart)
        print("Your Department no. is", self.dept_no)


class Student (Person, Department):
    def read_info(self):
        self.roll = int(input("Enter your Roll no. :"))
        self.sem = str(input("Enter your Semester :"))

    def show_info(self):
        print("Your roll no. is :", self.roll)
        print("Your Semester is :", self.sem)


class Faculty (Person, Department):
    def read_faculty(self):
        self.sal = int(input("Enter your salary :"))
        self.exp = int(input("Enter your experience :"))

    def show_faculty(self):
        print("The salary of the faculty is : ", self.sal)
        print("The faculty has the experience of", self.exp, "Years.")


if __name__ == '__main__':
    ch = int(input("Enter your choice:\n1. Student \n2.Faculty"))
    match ch:
        case 1:
            s = Student()
            s.readperson()
            s.readdept()
            s.read_info()
            s.showperson()
            s.showdept()
            s.show_info()

        case 2:
            f = Faculty()
            f.readperson()
            f.readdept()
            f.read_faculty()
            f.showperson()
            f.showdept()
            f.show_faculty()
