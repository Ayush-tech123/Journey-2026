import numpy as np

x = np.array([2, 4, 6])
y = np.array([0.5, 1, 1.5])

print(np.dot(x,y))

a = np.array([
    [2, 4, 6],
    [1, 2, 3],
    [0.5, 1, 1.5]
])

b = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

print(np.dot(a,b))

c = np.array([
    [1, 2, 3],
    [2, 3, 4]
])

print(c.shape)

d = np.array([
    [3, 4],
    [4, 5],
    [5, 6]
])

print(d.shape)
print(np.dot(c,d))

bias = 2.0
prediction = np.dot(x, y) + bias
print(prediction)
