cst = int(input("Enter your cost price:"))
sell = int(input("Enter your Selling price:"))

if sell > cst:
    print("You made a profit of", sell-cst)
else:
    print("You are in a loss of", cst-sell)
