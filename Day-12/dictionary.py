student = {"name" : "Ayush","age" : 19, "city" : "Ujjain"}
print(student["name"])
print(student["age"])
print(student["city"])

for key in student:
    print(key)

for value in student.values():
    print(value)

for items in student.items():
    print(items)

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(5):
    for j in range(3):
        print(i, j)

for i in range(3):
    for j in range(4):
        print("*", end="")
    print()
