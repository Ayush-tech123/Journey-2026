import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    [1, 3, 5],
    [2, 4, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 7, 9]
], dtype=float)

y = np.array([5, 10, 15, 20, 25], dtype=float).reshape(-1, 1)

w = np.ones((3, 1), dtype=float)
b = 0.0
lr = 0.1

losses = []

for i in range(100):
    
    y_pred = x @ w + b

    loss = np.mean((y - y_pred) ** 2)
    losses.append(loss)

    w_grad = (-2 / len(y)) * (x.T @ (y - y_pred))
    b_grad = np.mean(-2 * (y - y_pred))

    w -= lr * w_grad
    b -= lr * b_grad

print("final prediction:\n", y_pred)

plt.plot(losses)
plt.xlabel("Iteration")
plt.ylabel("Mean Squared Error")
plt.show()


