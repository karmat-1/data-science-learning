# Manipulating Arrays using Numpy (creating matric)
import numpy as np

# Element-wise Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a+b)
print(a * b)
print(a / b)

# Mathematical Operation
arr = np.array([4, 16, 25])
print(np.sqrt(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))

# Array Indexing
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])

# Array Slicing

print(arr[1:4])
print(arr[3:])

# Array Reshaping

reshaped = arr.reshape(2,3)
print(reshaped)