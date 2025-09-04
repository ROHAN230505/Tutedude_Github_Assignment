sal = float(input("Enter the amount of salary:"))

if (sal <= 150000):
    print("No TAX required.")
elif (sal >= 150001 and sal <=300000):
    print("The tax is:", (10/100)*sal)
elif(sal >= 300001 and sal <= 500000):
    print("The TAX is:", (20/100)*sal)
else:
    print("The TAX is:", (30/100)*sal)
