
class Employee:
    def __init__(self):
        self.empid = 101
        self.empname = "Sameera"

class Project(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.language = "Python"


class Team(Project):
    def __init__(self):
        Project.__init__(self)
        self.team_no = 5

    def display(self):
        print("Employee ID :", self.empid)
        print("Employee Name :", self.empname)
        print("Programming Language :", self.language)
        print("Team Number :", self.team_no)

obj = Team()
obj.display()
