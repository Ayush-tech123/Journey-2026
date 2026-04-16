import numpy as np

x = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

y = np.array([3, 6, 9, 12, 15])

w = np.array([0.0, 0.0])

learning_rate = 0.01

y_pred = x.dot(w)
print(x.T.dot(y - y_pred) / len(y)) 

for i in range(100):
    y_pred = x.dot(w)
    error = np.mean((y - y_pred) ** 2)
    gradient = -2 * x.T.dot(y - y_pred) / len(y)
    w = w - learning_rate * gradient

    if i % 1 == 0:
        print("step", i, "w =", w, "error =", error)
        
print(gradient)
print(error)
print(y_pred)
print(x.shape)
print(w.shape)
print(y.shape)
print(y_pred.shape)