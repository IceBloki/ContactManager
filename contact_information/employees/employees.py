from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os


class Employee(ContactInfo):
    def __init__(self, name, surname, date_of_birth, email, phone, address, job_title, department):
        super().__init__(name, surname, date_of_birth, email, phone, address)
        self.job_title = job_title
        self.department = department
        self.relative_employee_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "employess.txt")
        
        self.employee = f"{self.name};{self.surname};{self.date_of_birth};{self.email};{self.phone};{self.address};\
            {self.job_title}:{self.department}"+ "\n"


   
    def set_info(self):
            return FileManager.file_writer(self.relative_employee_path, self.employee)
    
 
    def add_info(self):
            return FileManager.file_append(self.relative_employee_path, self.employee)
    
   
    def get_info(self):
            return FileManager.file_reader(self.relative_employee_path)