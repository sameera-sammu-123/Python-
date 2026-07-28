class Parent:

    def display(self):
        print("This is Parent Class")

class Child(Parent):

    def show(self):
        print("This is Child Class")

obj = Child()

obj.display()
obj.show()