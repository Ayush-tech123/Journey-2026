student = []
choice = -1

while choice != 3:
    print("1. Add Record")
    print("2. View all")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        names = input("Enter a name : ")
        ages = int(input("Enter an age : "))
        cities = input("Enter a city : ")

        student1 = {"name": names, "age": ages, "city": cities}
        student.append(student1)

    elif choice == 2:
        if not student:
            print("No records found")
        else:
            for s in student:
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("City:", s["city"])
                print("------------------")

    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid Input")
