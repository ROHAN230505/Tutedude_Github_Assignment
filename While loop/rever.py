num = int(input("Enter Any number:"))

n = 0

while(num != 0):
    r = num % 10
    n =  n * 10 + r
    num = num // 10
print("REVERSE IS :", n)