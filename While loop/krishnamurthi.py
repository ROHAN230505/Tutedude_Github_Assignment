import math
num = int(input("Enter any number:"))
num1 = num
n = 0

while num != 0:
    r = num % 10
    s = math.factorial(r)
    n = s + n
    num //= 10

print(n)


if n == num1:
    print("The given no. is krishnamurthy no.")
else:
    print("The given no. is not a KRISHNAMURTHY no.")
