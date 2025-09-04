num = int(input("Enter any number"))

lar = 0
lar2 = 0

while(num != 0):
    r = num % 10
    if (r > lar):
        lar2 = lar
        lar = r
    elif(r < lar and lar2 < r):
        lar2 = r

    num = num // 10

print("2nd Largest num is ", lar2)
