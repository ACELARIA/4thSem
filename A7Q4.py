class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            return combined_salary  
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            salary_difference = self.salary - other.salary
            return salary_difference
        return NotImplemented

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"


employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

salary_sum = employee1 + employee2
print(f"Salary Sum: {salary_sum}")  
salary_diff = employee1 - employee2
print(f"Salary difference: {salary_diff}")  

