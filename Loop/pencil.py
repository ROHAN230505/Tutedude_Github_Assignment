n = int(input("Enter the standard:"))

sum = 0

if (n <= 12 and n>=1):

    for i in range(1, n + 1, 1):
        sum = sum + i ** 2

    print("The no. of pencils are:", sum)
else:
    print("Invalid")