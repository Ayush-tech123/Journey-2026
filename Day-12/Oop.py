class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Ayush", 19)
s1.display()

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

c1 = Car("BMW", 120)
c1.show()

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


s1 = Students("Ayush", 19)
s2 = Students("Rahul", 21)

s1.show()
s2.show()

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def show(self):
        print(self.value)


c = Counter()
c.increment()
c.increment()
c.show()

class Test:
    count = 0

    def __init__(self):
        Test.count += 1

t1 = Test()
t2 = Test()
t3 = Test()

print(Test.count)

