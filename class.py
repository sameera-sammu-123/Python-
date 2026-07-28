class Student:

    def __init__(self, name, course,subject):
        self.name = name
        self.course = course
        self.subject = subject
    def display(self):
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("Subject is", self.subject)



s = Student("Sameera", "MCA", "python")
s.display()