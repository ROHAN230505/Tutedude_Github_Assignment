import pyttsx3


a = int(input("Enter your ATM PIN:"))
f = open("data.txt", "r")
s = int(f.read())
f.close()
if (a == s):
    f = open("balance.txt", "r")
    bal = int(f.read())
    f.close()
    print("Your balance is:", bal)

    ch = int(input("1. Withdrawal 2.Deposit 3.Pin Change 4.statement print "))
    if (ch == 1):
        amt = int(input("Enter the amount you want to withdraw:"))
        bal = bal - amt

        f = open("balance.txt", "w")
        f.write(str(bal))
        f.close()

        Vengine = pyttsx3.init()

        Vengine.say("Withdrawal Successful of", amt)

        Vengine.runAndWait()
    elif (ch == 2):
        amt = int(input("Enter the amount you want to deposit:"))
        bal = bal + amt

        f = open("balance.txt", "w")
        f.write(str(bal))
        f.close()

    elif (ch == 3):
        pin = int(input("Enter the new pin:"))

        f = open("data.txt", "w")
        f.write(str(pin))
        f.close()
else:
    print("invalid password")
