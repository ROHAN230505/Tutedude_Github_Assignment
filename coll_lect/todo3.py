list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(list)

for i in range(0, len(list)):
    list[i] = tuple (reversed(list[i]))

print(list)

list.sort()

print(list)

for i in range(0,len(list[i])):
    list[i] = tuple(reversed(list[i]))

print(list)
