num = int(input("Enter any number : "))

lar = 0

while (num != 0):
    r = num % 10
    if(r > lar):
        lar = r

    num //= 10

print("The largest digit is", lar)