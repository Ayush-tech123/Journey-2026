import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5], dtype = float)

y = np.array([3, 6, 9, 12, 15], dtype = float)

w = 1
b = 0
learning = 0.01

plt.scatter(x, y)

y_pred_initial = x * w + b
plt.plot(x, y_pred_initial)

for i in range(100):
    y_pred = x * w + b

    error = np.mean((y - y_pred) ** 2)

    gradient = np.mean(-2 * x * (y - y_pred))
    b_grad = np.mean(-2 * (y - y_pred))

    w = w - learning * gradient
    b = b - learning * b_grad

    print("step:", i, "w:", w,"b:", b, "error:", round(error, 2))

print(y_pred)
y_pred_final = x * w + b
plt.plot(x, y_pred)

plt.xlabel("x")
plt.ylabel("y")
plt.show()