import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype = float)

y_true = np.array([50, 55, 65, 70, 75], dtype = float)

w = 0.0
b = 0.0

def predict(x, w, b):
    return w * x + b

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

y_pred = predict(x, w, b)
loss = mse(y_true, y_pred)

print("Initial loss:", loss)

def gradients(x, y_true, y_pred):
    dw = np.mean(-2 * x * (y_true - y_pred))
    db = np.mean(-2 * (y_true - y_pred))
    return dw, db

learning = 0.001
epochs = 200
losses = []

for i in range(epochs):
    y_pred = predict(x, w, b)

    dw, db = gradients(x, y_true, y_pred)

    w = w - learning * dw
    b = b - learning * db

    if i % 100 == 0:
        loss = mse(y_true, y_pred)
        loss = mse(y_true, y_pred)
        losses.append(loss)

        print(f"Epoch {i}: loss={loss:.2f}, w={w:.2f}, b={b:.2f}")

print("Final weight:", w)
print("Final bias:", b)

print("Predictions:", predict(x, w, b))
print("Actual:", y_true)

import matplotlib.pyplot as plt

plt.plot(losses)
plt.title("Learning rate = 0.1")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

