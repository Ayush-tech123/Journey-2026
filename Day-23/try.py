import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype = float)
y_true = np.array([43, 47, 49, 46, 54, 59, 69, 80, 95, 100], dtype = float)

w = 0.0
b = 0.0

def predict(x, w, b):
    return w * x + b

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

y_pred = predict(x, w, b)
loss = mse(y_true, y_pred)

def gradients(x, y_true, y_pred):
    dw = np.mean(-2 * x * (y_true - y_pred))
    db = np.mean(-2 * (y_true - y_pred))
    return dw, db

learning = 0.01
epochs = 100000

for i in range(epochs):
    y_pred = predict(x, w, b)

    dw, db = gradients(x, y_true, y_pred)

    w = w - learning * dw
    b = b - learning * db

    if i % 100 == 0:
        loss = mse(y_true, y_pred)
        print(f"Epoch {i}: loss={loss:.2f}, w={w:.2f}, b={b:.2f}")

print("Final weight:", w)
print("Final bias:", b)

print("Predictions:", predict(x, w, b))
print("Actual:", y_true)
