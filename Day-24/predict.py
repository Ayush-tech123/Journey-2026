inputs = [1, 2, 3, 4, 5]
predicted = [3, 5, 7, 9, 11]
actual = [2, 4, 6, 8, 10]

def differences(predicted, actual):
    diff_list = []

    for i in range(len(actual)):
        diff = actual[i] - predicted[i]
        diff_list.append(diff)

    return diff_list

difference = differences(predicted, actual)
print(difference)

def squared_diff(difference):
    sq_dif = []
    for d in difference:
        sq_dif.append(d * d)
    return sq_dif

squared_difference = squared_diff(difference)
print(squared_difference)

def average_error(squared_dif):
    count = 0
    total = 0
    for s in squared_dif:
        total = total + s
        count += 1
    return total / count

avg_error = average_error(squared_difference)
print(avg_error)