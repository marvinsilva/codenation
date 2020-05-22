from abc import ABCMeta, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=ABCMeta):
    work_hours = 8

    @abstractmethod
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.__salary = salary
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        return self.salary * 0.15

    @classmethod
    def get_hours(cls):
        return cls.work_hours

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department.name = department


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
