class Circle:

    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2

c = Circle()
print(c.area(5))