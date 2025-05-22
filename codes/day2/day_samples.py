# Advance Numpy Operations
import numpy as np

# Array and scalar broadcasting in Numpy
arr = np.array([1, 2, 3])
print(arr + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print(matrix + vector)

# Aggregation Functions
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("sum:", np.sum(arr))
print("meam:", np.mean(arr))
print("max:", np.max(arr))
print("min:", np.min(arr))
print("standard deviation:", np.std(arr))
print("sum along rows:", np.sum(arr, axis=1))
print("sum along colums:", np.sum(arr, axis=0))

# Boolean Indexing and filtering
arr = np.array([1, 2, 3, 4, 5, 6])
evens = arr[arr % 2 == 0]
print("Even:", evens)

arr[arr > 0] = 0
print("Modified Array:", arr)

# Random Number generation and setiing seed
np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)


random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)
