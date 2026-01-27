numbers = [85, 90, 72, 88]

num1 = []
num2 = []

count = 0

for n in numbers:
    if n >= 80:
        num1.append(n)

for n in numbers:
    n = n * n
    num2.append(n)

for n in numbers:
    if n >= 80:
        count += 1

print(num1)
print(num2)
print(count)