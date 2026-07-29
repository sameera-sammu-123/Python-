
class Animal:
    def animal(self):
        print("Animal")

class Bird(Animal):
    def bird(self):
        print("Bird")


class Parrot(Bird):
    def parrot(self):
        print("Parrot")

obj = Parrot()

obj.animal()
obj.bird()
obj.parrot()
