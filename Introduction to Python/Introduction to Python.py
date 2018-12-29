# Assigning a variable
a = 1
# Printing
print(a)
# To get what data type the object is. Python data type can be float, int, str, bool
type(a)
# Bolean operator
a = True
# This results in abcd
c = 'ab' + 'cd'
a = [1, "wwd"]  # This creates a list with different element being different types
# Making list of lists. Here type(a) will return list
# NOTE: Python has a zero based indexing
a = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
a = range(1000)  # Makes an array with integers from 0 to 999
import sys

print(sys.getsizeof(5) * len(a))  # Prints the memory size of a
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a + b)  # Prints [1,2,3,4,5,1,2,3,4,5]
print(a[0])  # Returns 1
print(a[-1])  # Returns 5
print(a[0:2])  # Returns [1,2]
print(a[:3])  # Python starts from index zero
print(a[2:])  # Python ends at the last index
a[0:2] = ["e", "r"]  # Changes the first and second element
a = a + [2, 4, 6]  # Adds the element to list (At the end)
del (a[2])  # The third element is removed from the list

x = ["a", "b", "c", ]
y = x
y[1] = "z"
print(y)
print(x)  # The value of 2nd element also changes. This is because list stores the address of variable and
# not the variable itself
# To copy a list just do list_copy = copy[:]

a = [1, 2, 3, 4]
print(max(a))  # Returns maximum of the functions
print(round(a[0], 1))  # Rounds the function to given number of decimal places
# If you do not mention then it rounds nearest to zero decimal places
print(len(a))  # Prints the length of the list

sorted(A, reverse=True)  # To sort the list "A" in descending order
a = ['a', 1, 'b', 2, 'c', 3, 3]
print(a.index('b'))  # Returns index corrosponding to 'b' i.e. 2
print(a.count(3))  # Returns number of times 3 is repeated
a = 'yolo'
a = a.capitalize()  # The first letter is capitalize in the string a
a = a.replace("lo", "nolo")  # lo string is replaced with nolo. Available for strings only
a.append("me")  # Add an element in the list. The element is added at the end
a.reverse()  # Reverses the elements of the list
import numpy as np  # Imports numpy and name it as np

a = np.array([12, 2, 34])
from numpy import array  # Imports array function from numpy

a = array([12, 33, 4])

height = [24, 412, 5, 45, 234]
weight = [213, 4, 32, 345, 34]
np_height = np.array(height)  # Imports all the variable to a numpy array
np_weight = np.array(weight)  # Imports all the variable to a numpy array
print(np_weight / np_height)  # Prints the array with division being done element wise
print(np_weight + np_height)  # Prints the array with addition being done element wise
a = np.array([1, "abcd", True])  # Ends up changing all the elements to string. numpy array takes only one type of data
print(np_weight > 23)  # Prints the array with each element being boolean type
print(np_weight[np_weight > 23])  # Prints value (array format) in np_weight when value is greater than 23

a = np.array([[1, 2, 3, 4, 5], [4, 7, 3, 7, 3]])  # Creates a 2-D Array
print(a.shape)  # Prints the shape of the matrix (2,5) i.e. 2 rows and 5 coloums
print(a[0][2])  # Prints 0th row 2nd element
print(a[0, 2])  # Prints 0th row 2nd element
print(a[:, 1:3])  # Selects both the rows and then prints element in 1 and 2 coloum
print(a[1, :])  # Selects 1st row and prints it completely

print(np.mean(np_height))  # Prints the mean of np_height dataset
print(np.median(np_height))  # Prints the mean of np_height dataset

# Packages might have sub-packages too

from numpy import *  # This calls all the functions

height = [24, 412, 5, 45, 234]
h = np.array(height)  # Imports all the variable to a numpy array
h = h[h > 24]
print(h)
# NUMPY
# Adds support for Multi Dimensional Array
# Mathematical Functions

import numpy as np

a = np.array([1, 2, 3])  # 1D Array
a = np.array([[1, 2], [1, 5]])  # 2D Array
a = np.arange(1000)  # Creates a 1D Array from 0 to 999
print(a.ndim)  # Prints the dimensions of the array
print(a.itemsize)  # Size of each element in the array
print(a.dtype)  # Prints the data type of the array
print(a.shape)  # Prints the shape of the array
a = a.reshape(4, 2)  # Changes the number of rows and coloums in the array
print(a.max())  # Prints the max element
print(a.min())  # Prints the min element
print(a.sum())  # Prints the sum of elements

# PANDAS
# Handles data suited for data analysis