def great(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c


def main():
    a = int(input("Enter you no."))
    b = int(input("Enter you no."))
    c = int(input("Enter you no."))

    g = great(a,b,c)
    print("The greatest no. is ", g)

main()