inputs = [1, 2, 3, 4, 5]
actual = [3, 6, 9, 12, 15]

a = 2
c = 1

def predict_list(inputs, a , c):
    predictions = []
    for x in inputs:
        predictions.append(x * a + c)
    return predictions

def differences(predicted, actual):
    diff_list = []

    for i in range(len(actual)):
        diff = actual[i] - predicted[i]
        diff_list.append(diff)

    return diff_list

def squared_diff(difference):
    sq_dif = []
    for d in difference:
        sq_dif.append(d * d)
    return sq_dif

def average_error(squared_dif):
    count = 0
    total = 0
    for s in squared_dif:
        total = total + s
        count += 1
    return total / count

predicted = predict_list(inputs, a, c)
difference = differences(predicted, actual)
squared_difference = squared_diff(difference)
avg_error = average_error(squared_difference)

print("Predicted:", predicted)
print("Difference:", difference)
print("Squared difference:", squared_difference)
print("Average error:", avg_error)

a = 0
c = 0

for step in range(31):
    predicted = predict_list(inputs, a, c)
    difference = differences(predicted, actual)
    squared_difference = squared_diff(difference)
    avg_error = average_error(squared_difference)

    print("a:", a, "Error:", avg_error)

    a = a + 0.1
