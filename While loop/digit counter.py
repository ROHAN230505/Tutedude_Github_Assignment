num = int(input("Enter Any number:"))

n = 0
while(num != 0):
    num = num // 10
    n = n + 1

print(n)