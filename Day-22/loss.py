import numpy as np

y_true = np.array([100, 150, 200])
y_pred = np.array([90, 160, 180])

errors = y_true - y_pred
print(errors)

squared_errors = errors ** 2
print(squared_errors)

mse = np.mean(squared_errors)
print(mse)