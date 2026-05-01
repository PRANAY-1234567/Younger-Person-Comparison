class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print("Name   :", self.name)
        print("Age    :", self.age)

    def younger(self, t):
        if self.age < t.age:
            return self
        else:
            return t


p1 = Person("Akshay", 26)
p2 = Person("Saurabh", 30)

y = p1.younger(p2)

print("Younger person")
y.getInfo()
