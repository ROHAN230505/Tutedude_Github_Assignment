car = []

while(True):
    n = input("Enter car name")
    car.append(n)

    ch =input("Do you wish to ad more yes/no ?")
    if(ch=="no"):
        break

print(car)