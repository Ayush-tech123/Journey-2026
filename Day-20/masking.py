import numpy as np

data = np.array([85, 90, 72, 88, 95, 60])
print(data)

mask = data >= 80
print(mask)

filtered = data[mask]
print(filtered)

scores = np.array([
    [85, 90, 72],
    [88, 76, 95],
    [91, 89, 84]
])

print(scores)
print("-----------------------------------------------------")
print("high scores")
high_scores = scores[scores >= 85]
print(high_scores)

print("-----------------------------------------------------")
print("row means")
row_means = np.mean(scores, axis=1)
print(row_means)

print("-----------------------------------------------------")
print("print selected")
selected = scores[row_means >= 85]
print(selected)
