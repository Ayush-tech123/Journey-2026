choice = -1
name = input("Enter your name : ")

while choice != 3:
    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")
    print("4. Print Name")

    choice = int(input("Enter choice : "))

    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("Bye")
    elif choice == 3:
        print("Exiting...")
    elif choice == 4:
        print("Hello", name)
    else:
        print("Invalid Input")