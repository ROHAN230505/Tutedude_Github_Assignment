contact = {"Rohan": 9096195565,
           "Siddhant": 8459304532,
           "Harsh": 8411019083,
           "Yuvraj": 8897137243,
           "Kartik": 9856745321,
           "Kishor": 8459304532,
           "Ayush": 9963238973,
           "Aniruddha": 6538764983,
           "Rupesh": 7763564382,
           "Kulprit": 8897137240
           }

n = str(input("Enter the name you want to search:"))
if n in contact:
    print(contact[n])
else:
    print("Contact not available.")

