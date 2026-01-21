try:
    x = int(input("Enter a number : "))
    print(10/x)
except ValueError:
    print("You must enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")