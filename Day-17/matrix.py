import numpy as np

x = np.array([1, 2, 3, 4])
y = x[1:3]

y[:] = 99

print(x)
print(y)
