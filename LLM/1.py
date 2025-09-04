import numpy as np

# Create an array from 1 to 10
a = np.arange(1, 11)

# Multiply all elements by 2
b = a * 2

# Calculate and print the mean of the new array
print("Array:", a)
print("Mean:", np.mean(b))