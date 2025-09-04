num = int(input("Enter any number:"))
num1 = num
s = 0
p = 1

while (num != 0):
    r = num % 10
    p = p * r
    s = s + r
    num = num // 10

print("Product is ", p)
print("Sum is", s)

if (s == p):
    print(num1, "The number is a spy number.")
else:
    print(num1, "The number is not a spy number.")
