import numpy as np

py_list = [1, 2, 3, 4]
np_array = np.array([1, 2, 3, 4])

print(type(py_list))
print(type(np_array))

print(py_list * 2)
print(np_array * 2)

print(np_array + 10)
print(np_array * np_array)

a = np.array([1, 2, 3])
b = np.array([10, 20 ,30])

print(a + b)
print(a * b)