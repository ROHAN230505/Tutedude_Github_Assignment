for i in range(1, 6, 1):
    for j in range(1, 11, 1):
        if (j == 1 or j == 10 or 10 - i + 1<= j or j <= i):
            print(j, end = " ")
        else:
            print(" ", end = " ")
    print()
