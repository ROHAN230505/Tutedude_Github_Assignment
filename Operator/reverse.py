print("Enter any 4 digit no.")
num1 = int(input())

d = num1 % 10
c = (num1 // 10) % 10
b = (num1 // 100) % 10
a = (num1 // 1000) % 10

newnum1 = d * 1000 + c * 100 + b * 10 + a * 1
print(newnum1)
