import numpy as np

# Creating a 1D array
x = np.array([1, 2, 3])

# Creating a 2D array
y = np.array([[1, 2], [3, 4]])

# Creating a 3D array
z = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(x)
print(y)
print(z)


import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Range of elements:",arr[1:4])
#all rows secomd clm
print("multidimensional slicing:",arr[:,1])


import numpy as np

a1_zeros = np.full((3, 3),5)
a2_ones = np.ones((2, 2))
a3_range = np.arange(0, 10, 2)

print(a1_zeros)
print(a2_ones)
print(a3_range)


import numpy as np

# Create a 1D array
arr1d = np.array([10, 20, 30, 40, 50])

# Single element access
print("Single element access:", arr1d[2])

# Negative indexing
print("Negative indexing:", arr1d[-1])

# Create a 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Multidimensional array access
print("Multidimensional array access:", arr2d[1, 0])


zeros = np.zeros((2, 3))
ones = np.ones((2, 3))

print(zeros)
print(ones)


# arr = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
# print(type(arr))
# print(array.shape(arr))

a1 = np.arange(0,10,2)
print=(a1)


# import numpy as np

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# # Getting second row
# print("Range of Elements:", arr[1])

# # Getting all rows, second column
# print("Multidimensional Slicing:", arr[:, 1])




# import numpy as np

# arr = np.linspace(0, 10, 5)
# print(arr)




# np.array() – Create an array from a list

# import numpy as np
# a = np.array([1, 2, 3])

# np.zeros() – Create an array filled with 0
# np.zeros((2, 3))

# np.ones() – Create an array filled with 1
# np.ones((3, 3))

# np.arange() – Create values in a range
# np.arange(1, 10, 2)

# np.linspace() – Create evenly spaced numbers
# np.linspace(0, 1, 5)




# 2. Mathematical Functions

# NumPy supports many mathematical operations:

# np.add(x, y) – Addition
# np.subtract(x, y) – Subtraction
# np.multiply(x, y) – Multiplication
# np.divide(x, y) – Division
# np.sqrt() – Square root
# np.power() – Power
# np.sin() – Sine function
# np.cos() – Cosine function
# np.log() – Logarithm




# 3. Statistical Functions

# Used for data analysis:

# np.mean() – Find mean
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# mean_value = np.mean(arr)

# print("Mean:", mean_value)

# np.median() – Find median

# np.std() – Standard deviation

# np.var() – Variance

# np.min() – Minimum value

# np.max() – Maximum value



# 4. Shape & Reshaping Functions

# np.shape() – Find shape
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# print("Shape:", np.shape(arr))

# # np.reshape() – Change array shape

# a = np.array([[1,2],[3,4]])

# print(a.reshape(4))

# np.transpose() – Transpose array

# np.flatten() – Convert multi-d array to 1D




# 5. Random Functions

# np.random.rand() – Random numbers between 0 and 1

# np.random.randint() – Random integers

# np.random.randn() – Random values from normal distribution




# 6. Useful Array Functions

# np.where() – Find elements based on condition
# np.sort() – Sort array
# import numpy as np

# a =np.array([4,3,2,])
# a2 =np.sort(a)
# print(a2)
# np.unique() – Find unique values
# np.argmax() – Index of maximum value
# np.argmin() – Index of minimum value