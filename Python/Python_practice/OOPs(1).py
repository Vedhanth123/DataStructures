class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        print(params)
        return cls(params[0], params[1], params[2])

    @classmethod
    def form_dash(cls, string):
        par = string.split("-")
        return cls(par[0], par[1], par[2])

    @staticmethod
    def print_hello(string):
        print(f"THe hello {string} ")


class programmer(Employee):

    def __init__(self, aname, asalary, arole, languages_prog):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages_prog

    def print_details_prog(self):
        print(self.name, self.role, self.salary, self.languages)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.form_dash("Karan-480-vesamount")
