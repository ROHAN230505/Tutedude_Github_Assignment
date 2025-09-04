# First we take the String as the input form the user Separately
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))

# Now we concatenate the first and the last name
full_name = first_name + " " + last_name

# Now we print the personalized greeting message using the full name.
print(f"\nHello, {full_name}! Welcome to the Python program.")
