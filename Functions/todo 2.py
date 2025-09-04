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


def main():
    ch =int(input("ENTER YOUR CHOICE"))

    if(ch == 1):
        fact()
    else:
        rev()

main()