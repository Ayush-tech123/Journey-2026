class Test:
    count = 10

a = Test()
b = Test()

a.count = 99

print(a.count)
print(b.count)
print(Test.count)

class Demo:
    value = 5

obj = Demo()

print(obj.value)

obj.value = 20

print(obj.value)
print(Demo.value)

class Person:
    def show(x):
        print("Self is:", x)

p = Person()
p.show()