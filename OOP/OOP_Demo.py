class Employee:
    num_of_emps = 0
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return(f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
     
# instantiate an employee
emp_1 = Employee('Nikki','Xiao',10000)

# apply raise amount of instance
emp_1.apply_raise()
print(emp_1.pay)

# modify class variable
emp_1.set_raise_amt(1.06)

# instantiate employees
emp_2 = Employee('Test','Xiao',20000)
emp_3 = Employee.from_string('Eldora-Xiao-30000')

# class variable has been modified
print(Employee.raise_amt,emp_1.raise_amt, emp_2.raise_amt)
print(Employee.num_of_emps)

# check instantiated by class method
print(emp_3.full_name())

# static method, not related to class or instance parameter
from datetime import date
is_or_not = '' if Employee.is_workday(date.today()) else 'not'
print(f'Today is {date.today()}, it is {is_or_not} weekday')



class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Dev_Nikki','Xiao',40000,'Python')
dev_1.apply_raise()
print(dev_1.full_name(), 'is using', dev_1.prog_lang, 'and her pay is', dev_1.pay)

class Manager(Employee):
    raise_amt = 1.20
    def __init__(self, first, last, pay, emps=None):
        self.first = first
        self.last = last
        self.pay = pay

        if emps is None:
            self.emps = []
        else:
            self.emps = emps


    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def rmv_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emps(self):
        for emp in self.emps:
            print('-->', emp.full_name)

    
    # decorator
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print(f'Deleted Name of "{self.full_name}" !!!')
        self.first = None
        self.last = None

    # special (magic/dunder) method
    def __repr__(self) -> str:
        return 'Manager(full name:{}, email:{})'.format(self.full_name,self.email)   
    
    def __str__(self) -> str:
        return f'Manager Information:\n first:{self.first};last:{self.last};pay:{self.pay};full name: {self.full_name}; email:{self.email};'
    
    def __len__(self):
        return len(self.full_name)




dev_2 = Developer('Dev_Test','Xiao',45000,'Java')
dev_3 = Developer('Dev_Eldora','Xiao',50000,'Python')
mgr_1 = Manager('Mananger','Wang',80000,[dev_1,dev_2])

mgr_1.add_emp(dev_3)

print(f'Below is {mgr_1.full_name}\'s subordinates:')
mgr_1.print_emps()

mgr_1.rmv_emp(dev_1)
print(f'Below is {mgr_1.full_name}\'s subordinates:')
mgr_1.print_emps()

# call the dunner method
print(mgr_1)
print(f'The length of "{mgr_1.full_name}" is ',len(mgr_1))


# decorator - @property
mgr_1.last = 'Li'
print(mgr_1) #attributes are changes except email before added decorator of "property" for email method

# decorator - @property and @func.setter
mgr_1.full_name = "Manager Liu"
print(mgr_1) #full name could not be changed due to it's a method name, should add full_name.setter decorator

# decorator - @property and @func.deleter
del mgr_1.full_name
print(mgr_1)




