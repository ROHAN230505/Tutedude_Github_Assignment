unit = int(input("Enter the amount of units consumed:"))

if(unit > 300):
    un = unit-300
    un2 = (unit - un) - 100
    un3= unit -(un+un2)
    print("The bill is",un*7 + un2 * 5 + un3*3)
elif(unit <= 300 and unit >=100):
    ut= (unit -100)
    ut2 = ut*5
    ut3=unit-ut
    print("the bill is", ut2 + ut3*3)

elif(unit >=0 and unit <=100):
    print("The bill is:",unit*3)
else:
    print("Invalid")
