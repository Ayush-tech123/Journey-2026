import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype = float)
y = np.array([3, 6, 9, 12, 15], dtype = float)

a = 1
learning_rate = 0.1

for i in range(20):
    y_pred = a * x
    error = np.mean((y - y_pred) ** 2)
    gradient = np.mean(-2 * x * (y - y_pred))
    a = a - learning_rate * gradient

    print("step", i, "a =", round(a,2), "error =", round(error,2))
