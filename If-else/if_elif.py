mon = int(input("Enter the no. of the month:"))

if (mon > 12 or mon < 0):
    print("PLEASE ENTER THE VALID MONTH  NUMBER.")
elif (mon >= 3 and mon <= 5):
    print("The season is summer.")
elif (mon >= 6 and mon <= 8):
    print("The season is Rainy.")
elif (mon >= 9 and mon<=11):
    print("The season is Autumn.")
else:
    print("The season is Winter.")