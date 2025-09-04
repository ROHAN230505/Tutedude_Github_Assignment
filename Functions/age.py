def getAge() -> int:
    age = int(input("enter your age"))
    return age


def show(age):
    if (age >= 18):
        print("YOU ARE ELIGIBLE TO VOTE.")
    else:
        print("YOU ARE NOT ELIGIBLE TO VOTE.")


def main():
    age = getAge()
    show(age)


main()
