import addition


def main():
    ch = int(input("Enter your choice\n1.Integer addition \n2.Float addition \n3.String addition"))

    match ch:
        case 1:
            a = int(input("Enter your number 1:"))
            b = int(input("Enter your number 2:"))
            addition.intadd(a, b)

        case 2:
            a = float(input("Enter you number 1:"))
            b = float(input("Enter your number 2:"))
            addition.floadadd(a, b)

        case 3:
            a = str(input("Enter your number 1:"))
            b = str(input("Enter your number 2:"))
            addition.stringadd(a, b)


main()
