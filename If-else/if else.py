print("Enter your age:")
age = int(input())
if(age>=18):
    print("Your are eligible to vote.")
else:
    print("your not eligible to vote. You can vote after",18-age,"years.")