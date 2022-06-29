class Employee():
    number_of_emp = 0  # Practice2
    rate_raise = 1.5  # Practice2

    def __init__(self, firstname, lastname, yearold) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email=firstname +'.'+ lastname +'@company.com'
        self.yearold = yearold
        Employee.number_of_emp += 1  # Practice2
    @property  #Practice6
    def email_func(self):
        return '{}.{}@company.com'.format(self.firstname, self.lastname)
    
    @property #Practice6
    def fullname(self):
        return self.firstname + ' ' + self.lastname
    
    @fullname.setter #Practice6
    def fullname(self,name):
       firstname,lastname=name.split(' ')
       self.firstname=firstname
       self.lastname=lastname
    
    @fullname.deleter #Practice6  
    def fullname(self):
       print ('Delete Name!')
       self.lastname=None
       self.firstname=None

    def raise_value(self):  # Practice2
        self.yearold = int(self.yearold * self.rate_raise)

    @classmethod  # [Practice3]
    def set_rate_raise(cls, amount):
        cls.rate_raise = amount

    @classmethod  # [Practice3]
    def from_string(cls, emp_str):
        first, last, year = emp_str.split('-')
        return cls(first, last, year)

    # [Practice3] Using like function and not relate to internal attribute
    @staticmethod
    def is_daywork(day):
        if day.weekday() == 5:
            return 'Saturday'
        elif day.weekday() == 6:
            return 'Sunday'
        return 'Working Day'
    def __repr__(self) -> str: #[Practice4]
        return 'Employee({}, {}, {})'.format(self.firstname,self.lastname,self.yearold)
    def __str__(self) -> str: #[Practice4]
        return '{} -  {}'.format(self.firstname,self.lastname)
    def __add__(self,other): #[Practice4]
        return self.yearold + other.yearold
    def __len__(self): #[Practice4] 
        return len(self.fullname())
class Developer(Employee): # [Practice4] 
    rate_raise = 2
    def __init__(self, firstname, lastname, yearold, pro_lang) -> None:
        super().__init__(firstname, lastname, yearold)
        self.pro_lang = pro_lang

class Manager(Employee): # [Practice4]     
    def __init__(self, firstname, lastname, yearold, emp_list=None) -> None:
        super().__init__(firstname, lastname, yearold)
        if emp_list is None:
            self.emp_list=[]
        else:
            self.emp_list=emp_list
    def add_emp(self,emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
    def remove(self,emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
    def print_emplist(self):
        for emp in self.emp_list:
            print('-->',emp.fullname)

def Practice1():
    # [Practice1] --Link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
    emp1=Employee('Thuan','Phan',1989)
    emp2=Employee('Thang','Thanh',2000)
    print(F'1. {emp1.firstname:<6} - {emp1.lastname}')
    print(F'2. {emp2.firstname:<6} - {emp2.lastname}')

def Practice2():
    # [Practice2] --Link: https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
    print("Emp Number:",Employee.number_of_emp)
    emp1=Employee('Thuan','Phan',1989)
    emp2=Employee('Thang','Thanh',2000)
    print ('Emp1:',emp1.lastname)
    print ('Emp2:',emp2.lastname)
    print ('Full Name 1: {}'.format(emp1.fullname()))
    print ('Full Name 2: ', emp2.fullname())
    emp1.raise_value()
    print('Raise Emp1: ', emp1.yearold)
    print("Emp Number:",Employee.number_of_emp)
    print ('Emp 1 infor: ', emp1.__dict__)

def Practice3():
    # [Practice3] --Link: https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
    emp1=Employee('Thuan','Phan',1989)
    emp2=Employee('Thang','Thanh',2000)
    Employee.set_rate_raise(1.7)
    print('Rate: ',Employee.rate_raise)
    str_emp1='Thuan1-Phan1-1988'
    str_emp2='Thuan2-Phan2-1987'
    new_emp1= Employee.from_string(str_emp1)
    new_emp2= Employee.from_string(str_emp2)
    print('Emp1 infor: ',new_emp1.firstname)
    print('Emp2 infor: ',new_emp2.firstname)
    import datetime
    my_date=datetime.date(2022,1,10)
    print(Employee.is_daywork(my_date))      

def Practice4():
    # -----Inheritance--------------------------------------------------
    # [Practice4] --Link: https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
    dev1=Developer('Thuan','Phan',1989,'')
    dev2=Developer('Thang','Thanh',2000,'')
    print('Dev1 Fullname: ',dev1.fullname)
    dev1.raise_value() # using variable in new class
    print('Dev1 yearold: ',dev1.yearold)
    # print(help(Developer))
    dev1 = Developer('Thuan', 'Phan', 1989, 'Python')
    dev2 = Developer('Thang', 'Thanh', 2000, 'C++')
    print('Program Language', dev1.pro_lang)
    mgr1 = Manager('Thuan2', 'Phan', 1989, [])
    mgr1.print_emplist()
    mgr1.add_emp(dev1)
    mgr1.print_emplist()
    print('--------------------------')
    mgr1.add_emp(dev2)
    mgr1.print_emplist()
    print('--------------------------')
    mgr1.remove(dev2)
    mgr1.print_emplist()
    print(isinstance(mgr1,Manager))
    print(issubclass(Manager,Employee))
    print(issubclass(Developer,Employee))
    print(issubclass(Developer,Manager))

def Practice5():
    # -----Special (Magic/Dunder)--------------------------------------------------
    # [Practice5] --Link: https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5
    emp1=Employee('Thuan','Phan',1989)
    emp2=Employee('Thang','Thanh',2000)
    print(emp1) #__str__
    print(emp1+emp2) #__add__
    print(len(emp1)) #__len__

def Practice6():
    # -----Property Decorators - Getter,Setter,Delete--------------------------------------------------
    # [Practice6] --Link: https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
    emp1=Employee('Thuan','Phan',1989)
    emp1.firstname='Thang'
    print ('Emp1 first name: ',emp1.firstname)
    print ('Emp1 email: ',emp1.email)
    print ('Emp1 FullName: ', emp1.fullname) # Normally call function like email_func(). But with @Property call function like email_func [remove '()']
    print ('Emp1 Email: ',emp1.email_func)
    
    emp1.fullname='Hoang Nguyen'
    print ('Emp1 first name: ',emp1.firstname)
    print ('Emp1 Email: ',emp1.email_func)
    
    del emp1.fullname
    print ('Emp1 first name: ',emp1.firstname)
    
    
if __name__ == '__main__':
    #Practice1()
    #Practice2()
    #Practice3()
    Practice4()
    #Practice5()
    #Practice6()
    













