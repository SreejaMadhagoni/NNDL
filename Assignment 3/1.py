'''
Neural Network Deep Learning
ICP 3
author: Sreeja Madhagoni
student ID: 700755861
email: sxm58610@ucmo.edu

In class programming:
1. Create a class Employee and then do the following
• Create a data member to count the number of Employees
• Create a constructor to initialize name, family, salary, department
• Create a function to average salary
• Create a Fulltime Employee class and it should inherit the properties of Employee class
• Create the instances of Fulltime Employee class and Employee class and call their member functions.
'''

# Created Employee class with name, family, salary and department
class Employee:
    # declared a data member to count the number of Employees
    count = 0
    salary_cnt = 0

    # constructor to initialize the object's attributes
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
        Employee.salary_cnt = Employee.salary_cnt + salary

    # declared average_salary function to return average salary
    def average_salary(self):
        return Employee.salary_cnt/Employee.count

# Created a Fulltime Employee class and inherited the properties of Employee class
class FulltimeEmployee(Employee):
    pass
# Created the instances of Fulltime Employee class and Employee class and calling their member functions.
fulltime_employee1 = FulltimeEmployee("Sreeja", "sam", 12000, "administration")
fulltime_employee2 = FulltimeEmployee("kartik", "Reddy", 10000, "HR")
print("Fulltime Employees average salary using member function: {}".format(
    fulltime_employee2.average_salary()))
employee1 = Employee("Joy", "Kat", 6000, "HR")
employee2 = Employee("Jim", "Rocky", 8000, "Associate")
print("Employees average salary using member function: {}".format(
    employee1.average_salary()))
