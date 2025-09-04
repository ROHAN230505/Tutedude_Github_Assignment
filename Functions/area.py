def area(l, b):
    are = l * b
    return are


def main():
    l = int(input("Enter the Length"))
    b = int(input("Enter the Breadth"))
    are = area(l, b)
    print("The area is :", are)


main()
