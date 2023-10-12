from contact_information.contact_info import ContactInfo
from file_manager.file_manager import FileManager
import os


class Customer(ContactInfo, FileManager):
    def __init__(self, name, surname, date_of_birth, email, phone, address, occupation):
        super().__init__(name, surname, date_of_birth, email, phone, address)
        self.occupation = occupation
        self.relative_coustumer_path = os.path.join(os.path.dirname(os.path.abspath("ContactManager")), "file_manager", "customers.txt")
        self.customer = f"{self.name};{self.surname};{self.date_of_birth};{self.email};{self.phone};{self.address};{self.occupation}"+ "\n"
    
    
    def set_info(self):
            return FileManager.file_writer(self.relative_coustumer_path, self.customer)
   
    def add_info(self):
            return FileManager.file_append(self.relative_coustumer_path, self.customer)
   
    def get_info(self):
            return FileManager.file_reader(self.relative_coustumer_path)