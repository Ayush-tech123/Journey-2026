def predict(x, a, b):
    return x * a + b

x_values = [1, 3, 5, 7, 9]
a = 2
b = 1

results = []

for x in x_values:
    y = predict(x, a, b)
    results.append(y)

print(results)

actual = [3, 5, 7, 9, 11]

errors = []

for i in range(len(actual)):
    diff = actual[i] - results[i]
    errors.append(diff)

print(errors)

squared = []

for e in errors:
    squared.append(e * e)

print(squared)

total = 0
for s in squared:
    total += s

average = total / len(squared)
print(average)

