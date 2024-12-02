"""
Class documentation template example.

Attributes:
    attribute_name (type): Description of the attribute.

Methods:
    method_name(param1: type, param2: type) -> return_type:
        Description of what the method does.
        
        Args:
            param1 (type): Description of param1.
            param2 (type): Description of param2.
            
        Returns:
            return_type: Description of what is returned.
            
        Raises:
            ErrorType: Description of when this error is raised.
"""
# import datetime

# class Person:
#     # Constructor for class Person
#     # This is called when the instance is called ie a = Person(...args)
#     # The parameter should be passed based on constructor parameters.
#     def __init__(self, firstname, lastname, sex, age):
#       a  self.lastname = lastname
#         self.firstname = firstname
#         self.sex = sex
#         self.today_time = int(str(datetime.datetime.today()).split('-')[0])
#         self.age = age

#     def name(self):
#         return f'{self.firstname} {self.lastname}'
    
#     def cal_dob(self):
#         return self.today_time - int(self.age)


# p = Person('Nikita', 'RC', 'F', 24)
# print(p.name())
# print(p.cal_dob())
# # print(str(datetime.datetime.today()).split(' ')[0].split('-')[:-1])

# s = Person('Saman', 'Shrestha', 'M', 25)
# print(s.name())
# print(s.cal_dob())


class Employee:
    def __init__(self, name, employee_id, salary, dob):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.dob = dob
     

    def get_annual_salary(self):
        return self.salary * 12

    def give_raise(self, amount):
        # self.salary += amount
        self.salary = self.salary + amount
        return self.salary
    
    def calcuate_age(self):
        age= 2024 - self.dob
        return age




# Get employee name, employee id and salary from user and show 
Name= input('Enter Employee name:')
id=input('Enter employee id:')
salary=int(input('Enter the Salary of the employee:'))
dob=int(input('Enter the Date of birth employee'))
# print(f'{Name} {salary} {id}')

# # Example usage
e = Employee(Name, id, salary,dob)
print(f"Employee: {e.name}")
print(f"Annual Salary: ${e.get_annual_salary()}")
print(f"After raise: ${e.give_raise(500)}")
print(f"Age:{e.calcuate_age()}")

# class bank_Account:
#    def _init_(self,name ,balance ):
#     self.name = name
#     self.balance = balance

#     def account_holder(self):
#      return self.name

# n=bank_Account(name,balance)
# print(f"Name of Account:${n.account_holder()}")
   




