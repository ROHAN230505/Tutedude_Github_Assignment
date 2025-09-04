print("Enter any 3 digit no.")
num1=int(input())
rev=0

while num1 !=0:
    digit =num1%10
    rev=rev*10+digit
    num1= num1 // 10

print("Reversed number is",rev)