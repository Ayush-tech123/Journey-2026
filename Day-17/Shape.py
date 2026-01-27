import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])

print(a.shape)
print(b.shape)
print(a.ndim)
print(b.ndim)

print(a[0])
print(a[1:3])

a[1:3] = 100
print(a)

arr = np.array([10, 20, 30, 40])
print(arr + 5)

c = np.array([1, 2, 3, 4])
d = np.array([10, 20, 30, 40])
print(c + d)