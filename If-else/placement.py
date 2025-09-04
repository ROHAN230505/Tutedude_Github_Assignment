cse = int(input("Enter the no. of students placed COMPUTER SCIENCE & ENGINEERING:"))
ece = int(input("Enter the no. of students placed in ELECTRONICS & COMMUNICATION ENGINEERING :"))
mec = int(input("Enter the no. of students placed in MECHANICAL ENGINEERING:"))

if (cse < 0 or ece < 0 or mec < 0):
    print("Entered value is invalid.")
elif (cse == 0 and ece == 0 and mec == 0):
    print("Zero placement this year for COMPUTER SCIENCE, ELECTRONICS & COMMUNICATION and MECHANICAL ENGINEERING")
elif (cse > ece and cse > mec):
    print("COMPUTER SCIENCE ENGINEERING has the highest placement.")
elif (ece > cse and ece > mec):
    print("ELECTRONICS & COMMUNICATION ENGINEERING has the highest placement.")
elif (mec > cse and mec > ece):
    print("MECHANICAL ENGINEERING has the highest placement.")
elif (cse == ece and cse > mec):
    print("COMPUTER SCIENCE ENGINEERING and ELECTRONICS & COMMUNICATION ENGINEERING have same placements.")
elif (cse == mec and cse > ece):
    print("COMPUTER SCIENCE ENGINEERING and MECHANICAL ENGINEERING have same placements.")
elif (ece == mec and ece > cse):
    print("MECHANICAL ENGINEERING and ELECTRONICS & COMMUNICATION ENGINEERING have the same placements. ")
else:
    print("no data")
