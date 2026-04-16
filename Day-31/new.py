def calculate_grade(marks):
    if marks < 100 and marks >= 96:
        grade = 'A+'
    elif marks < 96 and marks >= 91:
        grade = 'A'
    elif marks < 91 and marks >= 86:
        grade = 'A-'
    elif marks < 86 and marks >= 81:
        grade = 'B+'
    elif marks < 81 and marks >= 76:
        grade = 'B'
    elif marks < 76 and marks >= 71:
        grade = 'B-'
    elif marks < 71 and marks >= 66:
        grade = 'C+'
    elif marks < 66 and marks >= 61:
        grade = 'C'
    elif marks < 61 and marks >= 0:
        grade = 'F'
    return
    
Name = str(input("Enter students name : "))
Marks = int(input("Enter Marks : "))

while(Marks < 0 or Marks > 100):
    print("Wrong Input")
    Marks = int(input("Enter Marks : "))

G = calculate_grade(Marks)
print("Calculate another grade y/n")
check = input()
if check == 'y':    #Python doesnt have a goto statement hence my pseduocode and my code need to be broken in funtions.
