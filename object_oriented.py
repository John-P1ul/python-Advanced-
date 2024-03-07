class Person:
    def __init__(self, name="Sam", age="21"):
        self.n = name 
        self.a = age

p = Person()
p1 = Person("John", 19)
p2 = Person("Phina", 19)
print(p.n, p.a)
print(f"{p1.n}, is {p1.a} Years Old.")
print(p2.n, p2.a)