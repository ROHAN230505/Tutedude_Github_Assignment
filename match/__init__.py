ch = int(input("1.Dosa(100)\n2.Idli(50)\n3.Poha(30)\nEnter choice\n"))

match ch:
    case 1:
        print("----------DOSA-------------")
        plate = float(input("Enter no of plates "))
        bill = plate * 100
        print("please Pay Rs ", bill)
    case 2:
        print("----------Idli-------------")
        plate = float(input("Enter no of plates "))
        bill = plate * 50
        print("please Pay Rs ", bill)
    case 3:
        print("----------POHA-------------")
        plate = float(input("Enter no of plates "))
        bill = plate * 30
        print("please Pay Rs ", bill)
        pass
    case _:
        print("Invalid choice ")