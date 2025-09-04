print("Enter the amount of money:")
amt = int(input())

a = amt // 2000
amt = amt % 2000
b = amt // 500
amt = amt % 500
c = amt // 100
amt = amt % 100
d = amt // 50

print("2000 notes are", a)
print("500 notes are", b)
print("100 notes are", c)
print("50 notes are", d)
