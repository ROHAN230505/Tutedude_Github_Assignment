for i in range (1,6):

    for j in range (1, 6):
        if (i ==1 or i ==5 ):
            print("*"  , end = " ")
        elif (i == 2 and j == 4):
            print("*", end=" ")
        elif (i == 3 and j == 3):
            print("*", end=" ")
        elif (i == 4 and j == 2):
            print("*", end=" ")
        else:
            print(" ", end = " ")
    print()