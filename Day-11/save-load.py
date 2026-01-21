import sys
student = []
choice = -1
try:
    file = open("info.txt", "a+")
except FileNotFoundError:
    print("File opening failed")
    sys.exit()
while choice != 3:
    print("1. Add Record")
    print("2. View Record")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Choice must be a valid number")
        continue

    if choice == 1:
        name = input("Enter a name : ")
        try:
            age = int(input("Enter an age : "))
        except ValueError:
            print("Age must be a number")
            continue
        city = input("Enter a city : ")

        student1 = {"name": name, "age": age, "city": city}
        student.append(student1)

        file.write(f"{name},{age},{city}\n")

    elif choice == 2:
        file.seek(0)  
        content = file.read()
        print(content)

    elif choice == 3:
        print("Exiting...")
        file.close()

    else:
        print("Invalid Input")
