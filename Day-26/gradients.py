inputs = [1, 2, 3, 4, 5]
actual = [3, 6, 9, 12, 15]

def predict_list(inputs, a):
    preds = []
    for x in inputs:
        preds.append(a * x)
    return preds

def average_error(predicted, actual):
    total = 0
    for i in range(len(actual)):
        diff = actual[i] - predicted[i]
        total += diff * diff
    return total / len(actual)

a = 0.0
step = 0.1

for i in range(20):
    current_pred = predict_list(inputs, a)
    current_error = average_error(current_pred, actual)

    # try increasing a
    pred_up = predict_list(inputs, a + step)
    error_up = average_error(pred_up, actual)

    # try decreasing a
    pred_down = predict_list(inputs, a - step)
    error_down = average_error(pred_down, actual)

    if error_up < current_error:
        a = a + step
    elif error_down < current_error:
        a = a - step

    print("step", i, "a =", round(a,2), "error =", round(current_error,2))
