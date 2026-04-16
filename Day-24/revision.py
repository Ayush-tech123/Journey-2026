numbers = [12, 7, 19, 3, 25, 10, -5, 0, 18]

def Count_numbers(num):
    count = 0
    for n in num:
        count += 1
    return count

Count = Count_numbers(numbers)
print(Count)

def Sum_numbers(num):
    total = 0
    for n in num:
        total = total + n
    return total

Total = Sum_numbers(numbers)
print(Total)

def Mean_numbers(total , count):
    return total / count

Mean_num = Mean_numbers(Total , Count)
print(Mean_num)

def Min_numbers(num):
    minimum = num[0]
    for n in num:
        if n <= minimum:
            minimum = n
    return minimum

Minimum = Min_numbers(numbers)
print(Minimum)

def Max_numbers(num):
    maximum = num[0]
    for n in num:
        if n >= maximum:
            maximum = n
    return maximum

Maximum = Max_numbers(numbers)
print(Maximum)

def count_positive(num):
    count = 0
    for n in num:
        if n > 0:
            count += 1
    return count

positive = count_positive(numbers)
print(positive)

def count_negative(num):
    count = 0
    for n in num:
        if n < 0:
            count += 1
    return count

negative = count_negative(numbers)
print(negative)

def remove_invalid(num):
    valid = []
    for n in num:
        if n >= 0:
            valid.append(n)
    return valid

clean = []
clean = remove_invalid(numbers)
print(clean)

def mean_positive(valid):
    count = 0
    total = 0
    for v in valid:
        count += 1
        total = v + total
    return total / count

mean_post = mean_positive(clean)
print(mean_post)