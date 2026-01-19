name = []

choice = -1

while choice != 3:
    print("1. Add Name")
    print("2. Print All Names")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        student = input("Enter student name : ")
        name.append(student)
    elif choice == 2:
        for n in name:
            print(n)
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid Input")