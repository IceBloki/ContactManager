from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os


class Employee(ContactInfo):
    
    
    relative_employee_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "employess.txt")

    def __init__(self, name, surname, date_of_birth, email, phone, address, job_title, department):
        super().__init__(name, surname, date_of_birth, email, phone, address)
        
        try:
            Employee.counter = Employee.get_employee_counter()
        except FileNotFoundError:
             Employee.counter = 0
        except ValueError:
             Employee.counter = 0
        Employee.counter += 1


        self.job_title = job_title
        self.department = department
        self.employee = f"{self.counter}. {self.name}, {self.surname}, {self.date_of_birth}, {self.email}, {self.phone}, {self.address}, {self.job_title}, {self.department}"+ ";" + "\n"


   
    def set_info(self):
            return FileManager.file_writer(self.relative_employee_path, self.employee)
    
 
    def add_info(self):
            return FileManager.file_append(self.relative_employee_path, self.employee)
    
   
    def get_info(self):
            return FileManager.file_reader(self.relative_employee_path)
    
    def read_lines(self):
            return FileManager.read_lines(self.relative_employee_path)

    @classmethod
    def add_employee(cls):
        name = input("Enter employee name: ")
        surname = input("Enter employee surname: ")
        date_of_birth = input("Enter employee date of birth: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        address = input("Enter employee address: ")
        job_title = input("Enter employee occupation: ")
        department = input("Enter employee's department: ")
        employee = Employee(name, surname, date_of_birth, email, phone, address, job_title, department)
        print("Employee information has been added.")
        return employee
    

    @classmethod
    def print_employee_info(cls):
        employee_info = Employee.get_info(cls)
        print("Employee Information:")
        print(employee_info)


    @classmethod
    def get_employee_counter(cls):
        lines = Employee.read_lines(cls)
        for line in lines:
            fields = line.split(".")
            cls.counter = int(fields[0])  
        return cls.counter