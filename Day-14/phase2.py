numbers = []
count = 0
end = -1
total = 0

while end != 7:
    print("1. Add Entry")
    print("2. View all")
    print("3. Count")
    print("4. Mean")
    print("5. Minimum")
    print("6. Maximum")
    print("7. Exit")
    end = int(input("Enter the function you want : "))
    if end == 1:
        start = int(input("Enter the amount of entries you want to input : "))
        if start <= 0:
            break
        while start > 0:
            marks = int(input("Enter the marks : "))
            numbers.append(marks)
            count += 1
            start -= 1
    if end == 2:
        if count == 0:
            break
        for n in numbers:
            print(n)
        
    if end == 3:
        print(count)
    
    if end == 4:
        if count == 0:
            break
        for n in numbers:
            total = total + n
        print(total/count)
        total = 0

    if end == 5:
        if count == 0:
            break
        minimum = numbers[0]
        for n in numbers:
            if minimum >= n:
                minimum = n
        print(minimum)

    if end == 6:
        if count == 0:
            break
        maximum = numbers[0]
        for n in numbers:
            if maximum <= n:
                maximum = n
        print(maximum)

    if end == 7:
        print("Exiting...")
        break