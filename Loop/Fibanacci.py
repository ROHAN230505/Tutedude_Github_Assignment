n = int(input("Enter the Range:"))

f = 0
sum = 1

for i in range(1, n + 1, 1):
    print(f, end=" ")
    tot = f + sum
    f = sum
    sum = tot
