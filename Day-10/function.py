choice = -1
name = input("Enter your name : ")
def greet(name):
    print("Hello", name)
greet("Ayush")

def add(a,b):
    return a + b

result = add(10, 20)
print(result)

def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

def say_name():
    print("Hello", name)

while choice != 5:
    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Say Name")
    print("4. Add Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        say_hello()
    elif choice == 2:
        say_bye()
    elif choice == 3:
        say_name()
    elif choice == 4:
        a = int(input("Enter a number a : "))
        b = int(input("Enter a number b : "))
        sum = add(a,b)
        print(sum)
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid Input")