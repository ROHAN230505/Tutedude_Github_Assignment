list = ["nation", "12", "lol", "aba", "1221", "1231", "xyzx", "lab", "abc"]

count = 0

for i in list:
    if (len(i) >= 3 and i[0] == i[-1]):
        count = count + 1


print("The count is:", count)
