balance = 0


def readbalance():
    global balance
    balance = int(input("Enter your balance:"))


def withdraw(amt):
    global balance
    balance = balance - amt


def deposit(amt):
    global balance
    balance = balance + amt


def showbalance():
    global balance
    print("YOUR CURRENT BALANCE IS : ", balance)


def main():
    readbalance()
    ch = int(input("ENTER YOUR CHOICE: \n1. WITHDRAW \n2. DEPOSIT"))
    match ch:
        case 1:
            amt = int(input("ENTER THE AMOUNT TO WITHDRAW:"))
            withdraw(amt)

        case 2:
            amt = int(input("ENTER THE AMOUNT TO DEPOSIT:"))
            deposit(amt)

    showbalance()


main()
