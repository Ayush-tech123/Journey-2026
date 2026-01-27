def CountNumbers(numbers):
    total = 0
    for n in numbers:
        total += 1
    return total

def MeanNumbers(numbers):
    total = 0
    total_sum = 0
    for n in numbers:
        total += 1
        total_sum = total_sum + n
    return total_sum / total

def Minimum(numbers):
    minimum = numbers[0]
    for n in numbers:
        if minimum >= n:
            minimum = n
    return minimum

def Maximum(numbers):
    maximum = numbers[0]
    for n in numbers:
        if maximum <= n:
            maximum = n
    return maximum

numbers = [85,90,72,88]

c = CountNumbers(numbers)
m = MeanNumbers(numbers)
mi = Minimum(numbers)
ma = Maximum(numbers)

print(c)
print(m)
print(mi)
print(ma)