bal = int(input("Enter you Balance:"))

ch = int(input("1.withdrawal \n2.Deposit\n"))

match ch:
    case 1:
        amt = int(input("Enter the amount you want to Withdraw"))
        bal = bal - amt
        print("Your Balance is", bal)

    case 2:
        amt = int(input("Enter the amount you want to Deposit:"))
        bal = amt + bal
        print("You Balance is:", bal)

    case _:
        pass
