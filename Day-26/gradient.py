predicted = [1, 2, 3, 4, 5]
actual = [3, 6, 9, 12, 15]

#Make a self guessing gradient function
def gradient(predicted, actual):
    #Making a list of difference
    diff_list = []
    for i in range(len(actual)):
        diff = actual[i] - predicted[i]
        diff_list.append(diff)
    
    b = 0
    c = 0
    for d in diff_list:
        b += d
        c += 1
    error = b / c

    sq_diff = []
    for d in diff_list:
        sq = d * d
        sq_diff.append(sq)
    
    total = 0
    count = 0
    for s in sq_diff:
        total += s
        count += 1
    avg_error = total / count
    
    a = 1
    e = 0

    while error > 0:
        a += 0.1
        predictions = []

        for p in predicted:
            predictions.append(p * a + e)
        for d in diff_list:
            b += d
            c += 1
        error = b / c

    while error < 0:
        a -= 0.1
        predictions = []

        for p in predicted:
            predictions.append(p * a + e)
        for d in diff_list:
            b += d
            c += 1
        error = b / c

    print(predictions)

ml = gradient(predicted, actual)
