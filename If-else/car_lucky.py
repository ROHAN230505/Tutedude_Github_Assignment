import pyttsx3
car = int(input("Enter the car number:"))

a = car % 10             #2345  % 10 = 5
b = (car // 10) % 10       #2345  // 10) % 10= 4
c = (car // 100) % 10
d = (car // 1000)

sum = a + b + c + d
print(sum)

if car > 9999 or car < 999:
    print("The number is Invalid")
elif sum % 3 == 0 or sum % 5 == 0 or sum % 7 == 0:
    print("The car has a LUCKY NUMBER.")
else:
    print("The number is not lucky")