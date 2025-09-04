def getFullName(fname,sname,lname)->str:
    fn = fname + " " + sname + " " + lname
    return fn

def main():
    fname = str(input("Enter your first name:"))
    sname = str(input("Enter your second name:"))
    lname = str(input("Enter you last name:"))

    fn = getFullName(fname,sname,lname)
    print("The full name is:", fn)

main()