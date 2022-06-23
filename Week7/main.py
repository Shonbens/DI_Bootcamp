import numpy as np
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

lst = [1, 2, 3]

lst_array = np.array(lst)
print(lst)
print(lst_array)

# accessing single values
print(lst_array[0])
print(lst_array[0])

# 2-d array
lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2], [4, 4, 4, 4, 3]]
lst_2d_arr = np.array(lst_2d)

# the shape of the array
print(lst_2d_arr.shape)
print(lst_2d_arr)

# reshape of the array
lst_2d_arr = lst_2d_arr.reshape((5, 3))
print(lst_2d_arr.shape)
print(lst_2d_arr)

# flat into 1-d
lst_2d_arr = lst_2d_arr.reshape((15,))
print(lst_2d_arr.shape)
print(lst_2d_arr)

one_dimension = np.array([1, 2, 3, 4])
print(one_dimension[:])

two_dimension = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(two_dimension[:])
# specific column and index
print(two_dimension[1, 2])
# all values from specific column
print(two_dimension[:, 1])
# all values from specific row
print(two_dimension[1, :])

# create numpy array from range + reshape
print(np.arange(16).reshape((4, 4)))

one = np.array([1, 2, 3, 4])
print(np.amin(one))
print(np.std(one))
print(np.prod(one))
print(np.dot(one, one))
print(one + 4)

# 1 ,2, 4 ,5 don't do

# 3
print(np.zeros(10))
# 6
five = (np.zeros(10))
five[4] = 5
print(five)
# 7
print(np.arange(10, 50))
# 8
print(np.arange(0, 11)[::-1])
# 9
print(np.arange(9).reshape((3, 3)))
# 10
indices = ([1, 2, 0, 0, 4, 0])
print(np.nonzero(indices))
# 11
array_3D = np.identity(3)
print(array_3D)
# 12
x = np.random.random((3, 3, 3))
print(x)
# 13
z = np.random.random((10, 10))
print(np.amin(z))
print(np.max(z))
# 14
e = np.random.random(30)
print(np.mean(e))
# 15
f = np.ones((5, 5))
f[1:-1, 1:-1] = 0
print(f)
# 16
f = np.pad(f, pad_width=1, mode='constant', constant_values=0)
print(f)
# 17
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
# 18
g = np.diag([1, 2, 3, 4, 5])
print(g)
# 19
s = np.ones((3, 3))
s = np.zeros((8, 8), dtype=int)
s[1::2, ::2] = 1
s[::2, 1::2] = 1
print(s)
# 20

