import math


def fact():
    n = int(input("ENTER YOUR NUMBER:"))

    f = math.factorial(n)
    print("The factorial of ", n, "is", f)


def rev():
    n = int(input("Enter your number:"))
    no = n

    num = 0
    while (n != 0):
        r = n % 10
        num = num * 10 + r
        n = n // 10

    print("The reverse of", no, "is", num)


ch = int(input("Enter your choice:\n1.Factorial\n2.Reverse"))

match ch:
    case 1:
        fact()
    case 2:
        rev()
